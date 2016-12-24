from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse

from .models import Event, Person, Attendance
from .forms import RegisterForm

def index(request):
  event_list = Event.objects.filter(active=True).order_by('-date_time')
  context = {'event_list': event_list}
  return render(request, 'events/index.html', context)
  
def detail(request, event_id):
  event = get_object_or_404(Event, pk=event_id)
  if request.method == 'POST': # if this is a POST request we need to process the form data
      form = RegisterForm(request.POST)
      if form.is_valid():
          p_id = get_person_id(form)
          attend = Attendance(person_id = p_id, event_id = event_id)
          attend.save()
          return HttpResponseRedirect('/events/')
        
  else: # if a GET (or any other method) we'll create a blank form
      form = RegisterForm()
      return render(request, 'events/detail.html', {'event': event, 'form': form})

  return render(request, 'events/detail.html', {'event': event, 'form': form})

def get_person_id(form):
  f_email = form.cleaned_data['attendee_email']
  p = Person.objects.filter(email=f_email).first()

  if p is None:
    f_full_name = form.cleaned_data['attendee_name']
    p = Person(full_name=f_full_name, email=f_email)
    p.save()
  return p.id