from django.urls import path, include
from rest_framework.routers import DefaultRouter
from alias.views import UserAlias, SocialView, PaymentView, ContactView, LinkView
from rest_framework_nested import routers

app_name = "Alias"

user_alias = DefaultRouter()
user_alias.register(r'', UserAlias, basename='user_alias')

social = routers.NestedSimpleRouter(user_alias, r'', lookup='user_alias')
social.register(r'social', SocialView, basename='social')

payment = routers.NestedSimpleRouter(user_alias, r'', lookup='user_alias')
payment.register(r'payment', PaymentView, basename='payment')

contact = routers.NestedSimpleRouter(user_alias, r'', lookup='user_alias')
contact.register(r'contact', ContactView, basename='contact')

link = routers.NestedSimpleRouter(user_alias, r'', lookup='user_alias')
link.register(r'link', LinkView, basename='link')

urlpatterns = [
	path(r'', include(user_alias.urls)),
	path(r'', include(social.urls)),
	path(r'', include(payment.urls)),
	path(r'', include(contact.urls)),
	path(r'', include(link.urls)),
]
