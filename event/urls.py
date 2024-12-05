from . import views
from django.urls import path


urlpatterns = [
    
  #  path('event', views.event_detail, name='event_detail'),
    path('event', views.event_detail, name='event'),
        
          #  path('event', views.EventsPage.as_view(), name='event_list'),
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

