from django.contrib import admin
from .models import *

admin.site.register(BaseUser)
admin.site.register(Departman)
admin.site.register(Letter)
admin.site.register(Comment)
admin.site.register(History)
admin.site.register(FileHistory)
admin.site.register(CommentFile) 