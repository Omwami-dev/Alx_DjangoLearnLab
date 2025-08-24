from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Allow read-only access for any request.
    Write access only for the object's owner (author).
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions only for owner
        return getattr(obj, 'author', None) == request.user

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS are GET, HEAD, OPTIONS (read-only access)
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
