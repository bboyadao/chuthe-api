from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
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
