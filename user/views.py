from rest_framework import viewsets

from drf_spectacular.utils import extend_schema_view
from user.models import User
from user.docs import user_docs


@extend_schema_view(**user_docs)
class UserView(viewsets.ModelViewSet):
    model = User
    queryset = User.objects.all()


