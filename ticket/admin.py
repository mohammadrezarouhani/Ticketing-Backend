from django.contrib import admin
from .models import *

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=['edit','user','rank','has_message','photo']
    readonly_fields=['has_message']
    list_editable=['rank']
    list_per_page=10

    def edit(self,queryset):
        return 'Click Here to Edit '


@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    list_display=['edit','title','priority','sender','receiver','status']
    list_select_related=['sender','receiver']

    def edit(self,queryset):
        return 'Click Here to Edit '


class MessageFileInline(admin.StackedInline):
    max_num=10
    min_num=1
    extra=0
    model=MessageFile


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display=['edit','title','description_summary','sender','receiver','status','updated_at']
    list_display_links=['edit','description_summary']
    readonly_fields=['status','updated_at']
    inlines=[MessageFileInline]

    def description_summary(self,queryset):
        return queryset.description[:100]+'...' if len(queryset.description)>100 else queryset.description
    
    def edit(self,queryset):
        return 'Click Here to Edit'
    

@admin.register(MessageFile)
class MessageFileAdmin(admin.ModelAdmin):
    list_display=['edit','message','file','created_at']
    readonly_fields=['created_at']
    list_display_links=['edit']

    def edit(self,queryset):
        return 'Click Here to Edit'
    
class ArchiveFileInline(admin.StackedInline):
    max_num=10
    min_num=1
    extra=0
    model=ArchiveFile

    
@admin.register(Archive)
class ArchiveAdmin(admin.ModelAdmin):
    list_display=['edit','title','description_summary','owner','departman']
    list_select_related=['owner']
    list_editable=['title']
    inlines=[ArchiveFileInline]

    def description_summary(self,queryset):
        return queryset.description[:100]+'...' if len(queryset.description)>100 else queryset.description

    def edit(self,queryset):
        return 'Click Here to Edit '

@admin.register(ArchiveFile)
class ArchiveFileAdmin(admin.ModelAdmin):
    list_display=['edit','archive','file','created_at']
    readonly_fields=['created_at']
    list_display_links=['edit']

    def edit(self,queryset):
        return 'Click Here to Edit'
    

@admin.register(Departman)
class DepartmanAdmin(admin.ModelAdmin):
    list_display=['edit','title','description_summary']
    list_display_links=['edit']

    def description_summary(self,queryset):
        return queryset.description[:100]+'...' if len(queryset.description)>100 else queryset.description
    
    def edit(self,queryset):
        return 'Click Here to Edit'
    