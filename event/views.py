from django.shortcuts import render, get_object_or_404, reverse
from .models import Event
from django.utils.timezone import now


def home(request):
    # Fetch three events
    event = Event.objects.filter(is_public=True).order_by('event_date')[:3]
    return render(request, "base.html", {"event": event})

def event_detail(request, event_id):
    # Fetch a single event by ID
    event = get_object_or_404(Event, id=event_id)
    return render(request, "event.html", {"event": event})