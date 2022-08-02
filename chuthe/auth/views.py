from dj_rest_auth.views import LoginView as LV, LogoutView as LO, PasswordChangeView as PC, \
    PasswordResetConfirmView as PRC, PasswordResetView as PRV, \
    UserDetailsView as UDV  # noqa
from drf_spectacular.utils import extend_schema_view

from chuthe.auth.docs import login_docs, logout_docs


@extend_schema_view(**login_docs)
class LoginView(LV):
    pass


@extend_schema_view(**logout_docs)
class LogoutView(LO):
    pass


class PasswordChangeView(PC):
    pass


class PasswordResetConfirmView(PRC):
    pass


class PasswordResetView(PRV):
    pass


class UserDetailsView(UDV):
    pass
