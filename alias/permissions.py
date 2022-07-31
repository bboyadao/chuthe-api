from rest_framework.permissions import BasePermission


class ThemSelf(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user.pk == obj.user.pk
