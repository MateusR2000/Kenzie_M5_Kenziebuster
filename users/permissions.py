from rest_framework import permissions
from rest_framework.views import Request, View
from .models import User

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, req: Request, view: View):
        return(
             req.user.is_superuser
        )

class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(
            self, 
            req: Request, 
            view: View, 
            obj: User
        ):
            return obj == req.user