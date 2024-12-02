from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError

class Event(models.Model):
    RECUR_CHOICES = (
        ("none", "None"),
        ("daily", "Daily"),
        ("weekly", "Weekly"),
        ("monthly", "Monthly"),
        ("quarterly", "Quarterly"),
        ("yearly", "Yearly"),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=255, blank=True, null=True)
    event_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    recurrence = models.CharField(
        max_length=20, choices=RECUR_CHOICES, default="none"
    )  # New field for recurrence frequency
    capacity = models.PositiveIntegerField(blank=True, null=True)  # Maximum attendees
    rsvp_count = models.PositiveIntegerField(default=0)  # RSVPs
    is_public = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.event_date and self.event_date < now():
            raise ValidationError("Event date cannot be in the past.")
        if self.end_date and self.end_date < self.event_date:
            raise ValidationError("End date cannot be before event date.")

    class Meta:
        ordering = ["event_date"]  # Orders events by upcoming date

    def __str__(self):
        return self.title




