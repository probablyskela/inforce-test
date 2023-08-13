from rest_framework import permissions
from rest_framework.request import Request


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view):
        return bool(
            request.method in permissions.SAFE_METHODS
            or request.user
            and request.user.is_staff
        )
