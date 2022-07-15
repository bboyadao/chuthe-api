from rest_framework.permissions import BasePermission


class MySelf(BasePermission):
    def has_object_permission(self, request, view, obj):
        return True
