from rest_framework import permissions 
import pdb

class LetterPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.owner==request.user or obj.departman == request.user.departman


class LetterMessagePermission(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        return obj.receiver==request.user or obj.sender== request.user


class HistoryPermission(permissions.BasePermission):
     
     def has_object_permission(self, request, view, obj):
         return obj.owner == request.user or obj.departman == request.user.departman

