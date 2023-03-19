from django.contrib import admin
from .models import *
 
admin.site.register(Profile)
admin.site.register(Departman)
admin.site.register(Letter)
admin.site.register(Message)
admin.site.register(Archive)
admin.site.register(ArchiveFile)
admin.site.register(MessageFile) 