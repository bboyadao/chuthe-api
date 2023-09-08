from dj_rest_auth.registration.views import RegisterView as RegisterViewDefault
from dj_rest_auth.views import LoginView as LV, LogoutView as LO, PasswordChangeView as PC, PasswordResetConfirmView as PRC, PasswordResetView as PRV, UserDetailsView as UDV  # noqa
from drf_spectacular.utils import extend_schema_view

from chuthe.auth import docs


class RegisterView(RegisterViewDefault):
    pass


@extend_schema_view(**docs.login_docs)
class LoginView(LV):
    pass


@extend_schema_view(**docs.logout_docs)
class LogoutView(LO):
    pass


@extend_schema_view(**docs.change_password_docs)
class PasswordChangeView(PC):
    pass


@extend_schema_view(**docs.reset_password_confirm_docs)
class PasswordResetConfirmView(PRC):
    pass


@extend_schema_view(**docs.reset_password_docs)
class PasswordResetView(PRV):
    pass


@extend_schema_view(**docs.user_detail_docs)
class UserDetailsView(UDV):
    pass
