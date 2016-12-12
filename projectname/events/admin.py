from django.contrib import admin
from . import models

class EventAdmin(admin.ModelAdmin):
    fields = ['enabled', 'date_time', 'name', 'description']

admin.site.register(models.Event, EventAdmin)
admin.site.register(models.Person)
admin.site.register(models.Attendance)