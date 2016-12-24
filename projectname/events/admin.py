from django.contrib import admin
from . import models

class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'date_time', 'active']
    fields = ['active', 'date_time', 'name', 'description']

class PersonAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'birthday', 'email']
    
admin.site.register(models.Event, EventAdmin)
admin.site.register(models.Person, PersonAdmin)
admin.site.register(models.Attendance)
admin.site.register(models.Relationships)
