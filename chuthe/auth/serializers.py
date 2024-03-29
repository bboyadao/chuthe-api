try:
	from allauth.account import app_settings as allauth_settings
	from allauth.account.adapter import get_adapter
	from allauth.account.utils import setup_user_email
	from allauth.socialaccount.helpers import complete_social_login
	from allauth.socialaccount.models import SocialAccount
	from allauth.socialaccount.providers.base import AuthProcess
	from allauth.utils import email_address_exists, get_username_max_length
except ImportError:
	raise ImportError('allauth needs to be added to INSTALLED_APPS.')

from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.core.exceptions import ValidationError as DjangoValidationError
from django.urls import exceptions as url_exceptions
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views.decorators.debug import sensitive_post_parameters
from rest_framework import exceptions, serializers

sensitive_post_parameters_m = method_decorator(
	sensitive_post_parameters('password1', 'password2'),
)

UserModel = get_user_model()


class LoginSerializer(serializers.Serializer):
	username = serializers.CharField(required=False, allow_blank=True)
	# email = serializers.EmailField(required=False, allow_blank=True)
	password = serializers.CharField(style={'input_type': 'password'})

	def authenticate(self, **kwargs):
		return authenticate(self.context['request'], **kwargs)

	def _validate_email(self, email, password):
		if email and password:
			user = self.authenticate(email=email, password=password)
		else:
			msg = _('Must include "email" and "password".')
			raise exceptions.ValidationError(msg)

		return user

	def _validate_username(self, username, password):
		if username and password:
			user = self.authenticate(username=username, password=password)
		else:
			msg = _('Must include "username" and "password".')
			raise exceptions.ValidationError(msg)

		return user

	def _validate_username_email(self, username, email, password):
		if email and password:
			user = self.authenticate(email=email, password=password)
		elif username and password:
			user = self.authenticate(username=username, password=password)
		else:
			msg = _('Must include either "username" or "email" and "password".')
			raise exceptions.ValidationError(msg)

		return user

	def get_auth_user_using_allauth(self, username, email, password):
		from allauth.account import app_settings

		# Authentication through email
		if app_settings.AUTHENTICATION_METHOD == app_settings.AuthenticationMethod.EMAIL:  # noqa
			return self._validate_email(email, password)

		# Authentication through username
		if app_settings.AUTHENTICATION_METHOD == app_settings.AuthenticationMethod.USERNAME:  # noqa
			return self._validate_username(username, password)

		# Authentication through either username or email
		return self._validate_username_email(username, email, password)

	def get_auth_user_using_orm(self, username, email, password):
		if email:
			try:
				username = UserModel.objects.get(email__iexact=email).get_username()
			except UserModel.DoesNotExist:
				pass

		if username:
			return self._validate_username_email(username, '', password)

		return None

	def get_auth_user(self, username, email, password):
		"""
		Retrieve the auth user from given POST payload by using
		either `allauth` auth scheme or bare Django auth scheme.

		Returns the authenticated user instance if credentials are correct,
		else `None` will be returned
		"""
		if 'allauth' in settings.INSTALLED_APPS:

			# When `is_active` of a user is set to False, allauth tries to return template html
			# which does not exist. This is the solution for it. See issue #264.
			try:
				return self.get_auth_user_using_allauth(username, email, password)
			except url_exceptions.NoReverseMatch:
				msg = _('Unable to log in with provided credentials.')
				raise exceptions.ValidationError(msg)
		return self.get_auth_user_using_orm(username, email, password)

	@staticmethod
	def validate_auth_user_status(user):
		if not user.is_active:
			msg = _('User account is disabled.')
			raise exceptions.ValidationError(msg)

	@staticmethod
	def validate_email_verification_status(user):
		from allauth.account import app_settings
		if (
				app_settings.EMAIL_VERIFICATION == app_settings.EmailVerificationMethod.MANDATORY  # noqa
				and not user.emailaddress_set.filter(email=user.email, verified=True).exists()
		):
			raise serializers.ValidationError(_('E-mail is not verified.'))

	def validate(self, attrs):
		username = attrs.get('username')
		email = attrs.get('email')
		password = attrs.get('password')
		user = self.get_auth_user(username, email, password)

		if not user:
			msg = _('Unable to log in with provided credentials.')
			raise exceptions.ValidationError(msg)

		# Did we get back an active user?
		self.validate_auth_user_status(user)

		# If required, is the email verified?
		if 'dj_rest_auth.registration' in settings.INSTALLED_APPS:
			self.validate_email_verification_status(user)

		attrs['user'] = user
		return attrs


class LogoutRequestSerialiser(serializers.Serializer):
	refresh = serializers.CharField()


class ShitResponseSerialiser(serializers.Serializer):
	detail = serializers.CharField()
	status = serializers.IntegerField()


class RegisterSerializer(serializers.Serializer):
	username = serializers.CharField(
		max_length=get_username_max_length(),
		min_length=allauth_settings.USERNAME_MIN_LENGTH,  # noqa
		required=allauth_settings.USERNAME_REQUIRED,  # noqa
	)
	email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)  # noqa
	password1 = serializers.CharField(write_only=True)
	password2 = serializers.CharField(write_only=True)

	def validate_username(self, username):  # noqa
		username = get_adapter().clean_username(username)
		return username

	def validate_email(self, email):  # noqa
		email = get_adapter().clean_email(email)
		if allauth_settings.UNIQUE_EMAIL:  # noqa
			if email and email_address_exists(email):
				raise serializers.ValidationError(
					_('A user is already registered with this e-mail address.'),
				)
		return email

	def validate_password1(self, password):  # noqa
		return get_adapter().clean_password(password)

	def validate(self, data):  # noqa
		if data['password1'] != data['password2']:
			raise serializers.ValidationError(_("The two password fields didn't match."))
		return data

	def custom_signup(self, request, user):
		pass

	def get_cleaned_data(self):
		return {
			'username': self.validated_data.get('username', ''),
			'password1': self.validated_data.get('password1', ''),
			'email': self.validated_data.get('email', ''),
		}

	def save(self, request):
		adapter = get_adapter()
		user = adapter.new_user(request)
		self.cleaned_data = self.get_cleaned_data()  # noqa
		user = adapter.save_user(request, user, self, commit=False)
		if "password1" in self.cleaned_data:
			try:
				adapter.clean_password(self.cleaned_data['password1'], user=user)
			except DjangoValidationError as exc:
				raise serializers.ValidationError(
					detail=serializers.as_serializer_error(exc)
				)
		user.save()
		self.custom_signup(request, user)
		setup_user_email(request, user, [])
		return user
