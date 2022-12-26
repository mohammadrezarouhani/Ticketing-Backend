from django.contrib import admin
from .models import *

admin.site.register(BaseUser)
admin.site.register(Departman)
admin.site.register(Letter)
admin.site.register(LetterMessage)
admin.site.register(History)
admin.site.register(CommentFile)