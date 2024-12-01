from . import views
from django.urls import path

#urlpatterns = [
#    path('', views.EventsList.as_view(), name='event_list'),
#    path('event_id', views.event_detail(), name='event_detail'),
#]


urlpatterns = [
    path("events/", views.EventListView.as_view(), name="event_list"),  # List of all events
    path("events/<int:pk>/", views.EventDetailView.as_view(), name="event_detail"),  # Event details
 #   path("events/create/", views.EventCreateView.as_view(), name="event_create"),  # Create a new event
  #  path("events/<int:pk>/update/", views.EventUpdateView.as_view(), name="event_update"),  # Update an event
   # path("events/<int:pk>/delete/", views.EventDeleteView.as_view(), name="event_delete"),  # Delete an event
]

