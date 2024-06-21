from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Event
from .forms import EventForm


@login_required(login_url="login")
def index(request):
    query = request.GET.get("query")
    events = Event.objects.all()

    if query:
        events = events.filter(Q(title__icontains=query) | Q(location__icontains=query))

    context = {"events": events}
    return render(request, "mainapp/index.html", context)


@login_required(login_url="login")
def event_details(request, id):
    event = get_object_or_404(Event, pk=id)
    participants = event.user.all()
    context = {"event": event, 'participants': participants}
    return render(request, "mainapp/event_details.html", context)


@login_required(login_url="login")
def add_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("mainapp:home_page")
    else:
        form = EventForm()
    return render(request, "mainapp/add_event.html", {"form": form})


@permission_required("mainapp.delete_event")
def delete_event(request, id):
    event = get_object_or_404(Event, pk=id)
    event.delete()
    return redirect("mainapp:home_page")


@login_required(login_url="login")
def participate(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    event.user.add(request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required(login_url="login")
def unparticipate(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    event.user.remove(request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@permission_required("mainapp.change_event")
def remove_participant(request, event_id, user_id):
    event = get_object_or_404(Event, pk=event_id)
    user_to_remove = get_object_or_404(User, pk=user_id)
    event.user.remove(user_to_remove)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
