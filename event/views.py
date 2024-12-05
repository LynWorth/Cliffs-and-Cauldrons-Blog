from django.shortcuts import render, get_object_or_404, reverse
from .models import Event
from django.views.generic import ListView
# from django.views import generic, View
from django.utils.timezone import now



class EventsPage(ListView):
    model = Event
    template_name = "event/event_list.html"
    context_object_name = "event"

    def get_queryset(self):
        return Event.objects.filter(is_public=True).order_by('event_date')

    
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, "event/event.html", {"event": event})

    

