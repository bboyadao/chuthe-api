from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.github.views import GitHubProvider
from allauth.socialaccount.providers.linkedin_oauth2.views import LinkedInOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.oauth2.views import OAuth2LoginView, OAuth2CallbackView

from dj_rest_auth.registration.views import RegisterView, VerifyEmailView, ResendEmailVerificationView, \
    SocialLoginView, SocialConnectView  # noqa


class GoogleLogin(SocialLoginView):
    """
    Use Implicit Grant, use this
    https://accounts.google.com/o/oauth2/v2/auth?redirect_uri=http://localhost:8000/registry/google/&prompt=consent&response_type=code&client_id=351836093868-hkhm8bd22afhfkctt1ttv45s7sqhlbvn.apps.googleusercontent.com&scope=openid%20email%20profile&access_type=offline
    https://accounts.google.com/o/oauth2/v2/auth?redirect_uri=http://localhost:8000/registry/google/&prompt=consent&response_type=token&client_id=351836093868-hkhm8bd22afhfkctt1ttv45s7sqhlbvn.apps.googleusercontent.com&scope=openid%20email%20profile
    """
    adapter_class = GoogleOAuth2Adapter


class FacebookConnect(SocialConnectView):
    adapter_class = FacebookOAuth2Adapter


class LinkedinConnect(SocialConnectView):
    # https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id=86cothf2hm5863&scope=r_liteprofile&state=true&redirect_uri=http://localhost:8000/oauth/

    # https://www.linkedin.com/oauth/v2/accessToken?grant_type=authorization_code&redirect_uri=http://localhost:8000/oauth/&client_id=86cothf2hm5863&client_secret=rTvi522VqKQXTwoa&code=AQSMGWq_zRYFneX02vUpmZZzbzWTpKMQFYXOYX7ZkoMCnE9vHmLehPcxW1lRERGCngtasR0azBUheuXv8rdL2LaCKQPIPT3r34LgOpO0_KfyQuerOD_k0ARVw_Y_5BF-eqdvTRt4pW4HNau2xWAsE_U68tQn5tN9GdsVt4Jvl0RFkf3AXw1aUdJFtzy3dzrabeczNJyVODQEGKEoIro
    # https://www.linkedin.com/oauth/v2/accessToken?redirect_uri=http://localhost:8000/oauth/&grant_type=authorization_code&client_id=86cothf2hm5863&client_secret=rTvi522VqKQXTwoa&code=AQSGJveeO47hxZBYi3WQXirlkFvmselAhZJMJQsweRvbbGRrhNJtpNXCBun5vhXD0uU43JzHJQRF9eVlqRCYW1BLDC7hz5IOhK6SDcZ6x1sQ00LN-m_nMiT3sJBF9_JTZ5U-8elekR69saCiCRm7UYo32CuoUlgQqXVwG16X6N7W_9cY8IcTto7N-yDO3gmVJhpsDRXOBgEDX3o0QI4
    adapter_class = LinkedInOAuth2Adapter
    callback_url = "http://localhost:8000/oauth/"
    client_class = OAuth2Client


class GithubConnect(SocialConnectView):
    adapter_class = GitHubProvider
