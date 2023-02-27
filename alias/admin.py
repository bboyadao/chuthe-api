from django.contrib import admin
from alias.models import Alias, PaymentBrand, Links, ContactInformation, PaymentInformation

admin.site.register(Alias)
admin.site.register(PaymentBrand)
admin.site.register(Links)
admin.site.register(ContactInformation)
admin.site.register(PaymentInformation)

