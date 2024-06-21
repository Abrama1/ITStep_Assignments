from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Attendee
from .forms import AttendeeForm, EventForm
from django.db.models import Q


def index(request):
    query = request.GET.get("query")
    events = Event.objects.filter(Q(title__icontains=query) | Q(location__icontains=query)) if query else Event.objects.all()
    return render(request, "mainapp/index.html", {"events": events})


def event_details(request, id):
    event_info = get_object_or_404(Event, pk=id)
    attendees = event_info.attendees.all()
    return render(request, "mainapp/event_details.html", {"event": event_info, "attendees": attendees})


def add_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("mainapp:home_page")
    else:
        form = EventForm()
    return render(request, "mainapp/add_event.html", {"form": form})


def delete_event(request, id):
    event_to_delete = get_object_or_404(Event, pk=id)
    event_to_delete.delete()
    return redirect("mainapp:home_page")


def add_attendee(request, id):
    event = get_object_or_404(Event, pk=id)
    if request.method == "POST":
        form = AttendeeForm(request.POST)
        if form.is_valid():
            attendee = form.save(commit=False)
            attendee.event = event
            attendee.save()
            return redirect("mainapp:event_details", event.id)
    else:
        form = AttendeeForm()
    return render(request, "mainapp/add_attendee.html", {"form": form, "event": event})


def delete_attendee(request, id):
    attendee_to_delete = get_object_or_404(Attendee, pk=id)
    event = attendee_to_delete.event_id
    attendee_to_delete.delete()
    return redirect("mainapp:event_details", event) if event else redirect("mainapp:home_page")
