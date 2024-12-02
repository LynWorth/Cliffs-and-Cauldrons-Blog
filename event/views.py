from django.shortcuts import render
from .models import Event
from django.utils.timezone import now

def upcoming_events(request):
    events = Event.objects.filter(is_public=True, event_date__gte=now())
    recurring_events = events.exclude(recurrence="none")
    single_events = events.filter(recurrence="none")
    return render(request, "events.html", {"events": single_events | recurring_events})



# Create your views here.
def event_detail(request, event_id):
    
    #event = event.objects.all().order_by('-updated_on').first()

    queryset = Event.objects.filter(status=1)
    event = get_object_or_404(queryset, event_id = event_id)


    return render(
        request,
        "event/event_detail.html",
        {"event": event},
    )


class EventsList(generic.Listview):
    model = Event
    template_name = "event/index.html"
    paginate_by = 12