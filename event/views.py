from django.shortcuts import render
from .models import Event


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