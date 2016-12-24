from __future__ import unicode_literals
from datetime import datetime
from django.utils import timezone

from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=70)
    date_time = models.DateField('Event date time', default=timezone.now)
    description = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):           
        return self.name
    
    class Meta:
        ordering = ['-date_time']

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=15, blank=True, null=True)
    birthday = models.DateField(default=timezone.now, null=True)

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)
    
    class Meta:
        verbose_name_plural = 'People'
        ordering = ['last_name', 'first_name']
        
class Relationships(models.Model):
    guardians = models.ManyToManyField(Person, related_name='is_guardian')
    children = models.ManyToManyField(Person, related_name='is_child')
    
    def __str__(self):
        return "{1} is/are the guardian(s) of {0}".format(', '.join(str(x) for x in self.children.all()), ', '.join(str(x) for x in self.guardians.all()))
      
class Attendance(models.Model):
    person = models.ForeignKey(Person)
    event = models.ForeignKey(Event)
    signin_date = models.DateField('Sign In', default=timezone.now)
    signout_date = models.DateField('Sign Out', null=True, blank=True)
    
    def __str__(self):
        return "{0} is Attending the Event: {1}".format(self.person, self.event.name)
