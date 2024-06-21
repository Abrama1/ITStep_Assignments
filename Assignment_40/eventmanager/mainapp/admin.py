from django.contrib import admin
from .models import Attendee, Category, Event


class EventDetails(admin.ModelAdmin):
    list_display = ("title", "date", "location")


class AttendeeDetails(admin.ModelAdmin):
    list_display = ("name", "email", "event")


admin.site.register(Attendee, AttendeeDetails)
admin.site.register(Category)
admin.site.register(Event, EventDetails)
