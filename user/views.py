from rest_framework import viewsets

from drf_spectacular.utils import extend_schema_view
from rest_framework.decorators import action
from rest_framework.response import Response
from user.models import User
from user.docs import user_docs
from user.serializers import UserSer, RegSer
from user.throttles import AnonRegThrottle


@extend_schema_view(**user_docs)
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSer

    @action(detail=False,
            methods=["POST"],
            throttle_classes=[AnonRegThrottle],
            serializer_class=RegSer)
    def register(self, request, *args, **kwargs):
        return Response({})
