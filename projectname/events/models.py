from __future__ import unicode_literals
from datetime import datetime
from django.utils import timezone

from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=70)
    date_time = models.DateField('Event date time', default=timezone.now)
    description = models.TextField()
    enabled = models.BooleanField(default=True)

    def __str__(self):           
        return self.name
    
    class Meta:
        ordering = ['-date_time']

class Person(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name_plural = 'People'
      
class Attendance(models.Model):
    person = models.ForeignKey(Person)
    event = models.ForeignKey(Event)
    
    def __str__(self):
        return "{0} is Attending the Event: {1}".format(self.person.full_name, self.event.name)
