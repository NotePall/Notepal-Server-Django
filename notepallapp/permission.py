# custom permission to allow user access only their required data

from rest_framework import permissions

# This is the customized authourization for the user note
class IsNoteOwner(permissions.BasePermission):

    def has_permission(self, request):
        if request.user.is_authenticated: 
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        if obj.editor == request.user:
            return True
        return False

# This is the customized authourization for the user stucky note
class IsStickyNoteOwner(permissions.BasePermission):

    def has_permission(self, request):
        if request.user.is_authenticated: 
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        if obj.editor == request.user:
            return True
        return False