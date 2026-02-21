from django.contrib import admin
from .models import *

# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_created')

admin.site.register(Message, MessageAdmin)
admin.site.register(TelegramBot)