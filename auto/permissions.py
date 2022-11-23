from rest_framework import permissions 
import pdb

class TicketPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.owner==request.user or obj.departman == request.user.departman


class TicketMessagePermission(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        return obj.reciver==request.user or obj.sender== request.user


class TicketHistoryPermission(permissions.BasePermission):
     
     def has_object_permission(self, request, view, obj):
         return obj.owner == request.user or obj.departman == request.user.departman

