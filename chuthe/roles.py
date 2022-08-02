from django.db import models
from django.utils.translation import gettext as _


class Privacy(models.TextChoices):
    ADMIN = _("ADMINSTRATOR"), _("ADMINSTRATOR").title()
    STAFF = _("STAFF"), _("STAFF").title()
    PUBLIC = _("PUBLIC"), _("PUBLIC").title()
    USER = _("USER"), _("USER").title()
