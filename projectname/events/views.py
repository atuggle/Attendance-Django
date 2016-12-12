from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse

from .models import Event, Person, Attendance

def index(request):
  event_list = Event.objects.filter(enabled=True).order_by('-date_time')
  context = {'event_list': event_list}
  return render(request, 'events/index.html', context)