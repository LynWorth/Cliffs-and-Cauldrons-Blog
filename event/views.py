from django.shortcuts import render
from .models import Event
#from django.views.generic import ListView
from django.views import generic
from django.utils.timezone import now
from django.views.generic import DetailView



class EventsPage(generic.ListView):
    model = Event
    template_name = "event/event_list.html"
    context_object_name = "event_list"
    paginate_by = 6

    def get_queryset(self):
        return Event.objects.filter(is_public=True).order_by('event_date')
        print(queryset)  # Debugging output
        return queryset

class EventDetailView(DetailView):
    model = Event
    template_name = "event/event.html"
    context_object_name = "event"






#def event_detail(request, event_id):
#   event = get_object_or_404(Event, id=event_id)
#   return render(request, "event/event.html", {"event": event})


   

