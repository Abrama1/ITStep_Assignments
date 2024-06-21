from django.contrib import admin
from .models import Category, Event


class EventDetails(admin.ModelAdmin):
    list_display = ("title", "date", "location")


admin.site.register(Category)
admin.site.register(Event, EventDetails)
