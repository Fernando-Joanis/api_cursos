from rest_framework import permissions

class IsSuperUser(permissions.BasePermission):

    def has_permission(self, requets, view):
        if requets.method == 'DELETE':
            if requets.user.is_superuser:
                return True
            return False
        return True