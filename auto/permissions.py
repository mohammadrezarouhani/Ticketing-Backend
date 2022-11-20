from rest_framework import permissions 
import pdb

class TicketPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        pdb.set_trace()
        return super().has_object_permission(request, view, obj)