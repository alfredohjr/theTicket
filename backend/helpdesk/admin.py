from django.contrib import admin

# Register your models here.

from helpdesk.models import Sector, Ticket, Comment

admin.site.register(Sector)
admin.site.register(Ticket)
admin.site.register(Comment)