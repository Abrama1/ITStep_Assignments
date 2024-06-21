from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import UserRegisterForm
from django.contrib.messages import success
from django.contrib.auth.decorators import login_required
from mainapp.models import Event

def register(request):
    
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("mainapp:home_page")
        else:
            return render(request, "users/register.html", {"form": form})
    else:
        form = UserRegisterForm()
        return render(request, "users/register.html", {"form": form})

def logout_user(request):
    logout(request)
    return render(request, "users/logout.html")

@login_required(login_url="login")
def user_profile(request):
    return render(request, "users/profile.html")

@login_required(login_url="login")
def my_events(request):
    
    events = Event.objects.filter(user=request.user)
    
    return render(request, "users/myevents.html", {"events": events})