from django.contrib import admin
from .models import *

admin.site.register(BaseUser)
admin.site.register(Departman)
admin.site.register(Ticket)
admin.site.register(TicketMessage)
admin.site.register(TicketHistory)
admin.site.register(FileUpload)