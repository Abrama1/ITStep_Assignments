from django.urls import path
from . import views

app_name = "mainapp"

urlpatterns = [
    path("", views.index, name="home_page"),
    path("event_details/<int:id>/", views.event_details, name="event_details"),
    path("add_event/", views.add_event, name="add_event"),
    path("delete_event/<int:id>/", views.delete_event, name="delete_event"),
    path("participate_to_event/<int:event_id>/", views.participate, name="participate"),
    path("unparticipate_to_event/<int:event_id>/", views.unparticipate, name="unparticipate"),
    path("remove_participant/<int:event_id>/<int:user_id>/", views.remove_participant, name="remove_participant"),
]
