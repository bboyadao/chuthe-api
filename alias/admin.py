from django.contrib import admin
from alias.models import Alias, ValueAilasValue, PaymentBrand, PaymentAliasAttr, Links, ContactInformation

admin.site.register(Alias)
admin.site.register(ValueAilasValue)
admin.site.register(PaymentBrand)
admin.site.register(PaymentAliasAttr)
admin.site.register(Links)
admin.site.register(ContactInformation)

