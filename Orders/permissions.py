from rest_framework import permissions


class IsOwnerOfOrder(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # This is dummy permission check
        # to demonstrate overall permissions implementation

        # User objects first name and last name must be equal to Customer's first name and last name
        # this is just for demonstration purposes.
        # otherwise could be implemented better
        first_name_equals = obj.customer.first_name == request.user.first_name
        last_name_equals = obj.customer.last_name == request.user.last_name
        return first_name_equals and last_name_equals

    def has_permission(self, request, view):
        # This is dummy permission check
        # to demonstrate overall permissions implementation
        if request.method in permissions.SAFE_METHODS:
            return True

        return False