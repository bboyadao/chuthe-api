from django.contrib import admin
from alias.models import Alias, ValueAilasValue, PaymentBrand, PaymentAliasAttr

admin.site.register(Alias)
admin.site.register(ValueAilasValue)
admin.site.register(PaymentBrand)
admin.site.register(PaymentAliasAttr)


