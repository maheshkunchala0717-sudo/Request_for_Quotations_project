from rest_framework.permissions import BasePermission


class IsBuyer(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == "buyer"
        )


class IsSupplier(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == "supplier"
        )

class IsBuyerOwner(BasePermission):
    def has_object_permission(self,request,view,obj):
        return(request.user.is_authenticated and request.user.role=="buyer" and obj.buyer==request.user)


class IsSupplierOwner(BasePermission):
    def has_object_permission(self,request,view,obj):
        return(request.user.is_authenticated and request.user.role=="supplier" and obj.supplier==request.user)