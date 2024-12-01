from django.contrib import admin
from .models import Event
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


#@admin.register(Event)
#class EventAdmin(admin.ModelAdmin):
#    list_display = ("title", "event_date", "created_on")  # Fields to display in the admin list view
#    search_fields = ("title", "description")  # Fields for the search bar
#    list_filter = ("event_date",)  # Filters in the admin sidebar


from django_summernote.admin import SummernoteModelAdmin

@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)  # Specify fields to use the Summernote editor
