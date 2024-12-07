from . import views
from django.urls import path
from .views import EventsPage
from .views import EventDetailView

urlpatterns = [
    
    path('events/', views.EventsPage.as_view(), name='events'),

    path('events/<slug:slug>/', EventDetailView.as_view(), name="event_detail"),
]
































#urlpatterns = [
#    # List view for events
#    path('event', views.EventsPage.as_view(), name='event_list'),
#
#    # Detail view for a single event
#    path('event', views.event_detail, name='event_detail'),
#]




#urlpatterns = [
#    path('event/<int:event_id>/', views.event_detail, name='event_detail'),  # Detail view for a single event
#    path('events/', views.EventsPage.as_view(), name='events'),  # List view for all events
#]

