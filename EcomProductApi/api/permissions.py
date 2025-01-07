from rest_framework.permissions import BasePermission, SAFE_METHODS

#Custom permission to allow anyone to read product,all users can create Product but only the owner can edit or delete them.
class ProductPermission(BasePermission):
    def has_permission(self, request, view):
        #allow everyone to read
        if request.method in SAFE_METHODS:
            return True
        #allow only authenticated users create
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        # Allow everyone to read (GET, HEAD, OPTIONS)
        if request.method in SAFE_METHODS:
            return True
        # Allow only the owner to edit or delete
        return obj.user == request.user
    
#Custom Permission 
class OrderPermission(BasePermission):
    """
    Custom permission to only allow owners of an order to edit or delete it.
    All authenticated users can create orders.
    """

    def has_permission(self, request, view):
        # Allow authenticated users to perform 'GET' (read) and 'POST' (create)
        if request.method in SAFE_METHODS or request.method == 'POST':
            return request.user and request.user.is_authenticated
        
        # Prevent 'PUT', 'PATCH', 'DELETE' for everyone unless specified by object-level permission
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return request.user and request.user.is_authenticated
        
        return False

    def has_object_permission(self, request, view, obj):
        # Allow owners to read their own orders
        if request.method in SAFE_METHODS:
            return obj.user == request.user
        
        # Allow owners to delete or update their own orders
        if request.method in ['DELETE', 'PUT', 'PATCH']:
            return obj.user == request.user
        
        return False