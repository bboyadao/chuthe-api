from django.urls import re_path, include
from django.views.generic import TemplateView

from chuthe.auth.reg.views import RegisterView, VerifyEmailView, ResendEmailVerificationView, GoogleLogin, \
    LinkedinConnect, GithubConnect
from django.urls import path

urlpatterns = [
    path('', RegisterView.as_view(), name='rest_register'),

    path("google/", GoogleLogin.as_view(), name="google_login"),
    path("linkedin/", LinkedinConnect.as_view(), name="linkedin_login"),
    path("facebook/", GoogleLogin.as_view(), name="facebook_login"),
    path("github/", GithubConnect.as_view(), name="github_login"),
    path("social/", include("allauth.socialaccount.urls")),
    path('verify-email/', VerifyEmailView.as_view(), name='rest_verify_email'),
    path('resend-email/', ResendEmailVerificationView.as_view(), name="rest_resend_email"),

    # This url is used by django-allauth and empty TemplateView is
    # defined just to allow reverse() call inside app, for example when email
    # with verification link is being sent, then it's required to render email
    # content.

    # account_confirm_email - You should override this view to handle it in
    # your API client somehow and then, send post to /verify-email/ endpoint
    # with proper key.
    # If you don't want to use API on that step, then just use ConfirmEmailView
    # view from:
    # django-allauth https://github.com/pennersr/django-allauth/blob/master/allauth/account/views.py
    re_path(
        r'^account-confirm-email/(?P<key>[-:\w]+)/$', TemplateView.as_view(),
        name='account_confirm_email',
    ),
    path(
        'account-email-verification-sent/', TemplateView.as_view(),
        name='account_email_verification_sent',
    ),
]
