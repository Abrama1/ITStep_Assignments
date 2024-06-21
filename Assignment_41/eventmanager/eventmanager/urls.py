from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("mainapp.urls", namespace="mainapp")),
    path('register/', user_views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path('logout/', user_views.logout_user, name="logout"),
    path('profile/', user_views.user_profile, name="profile"),
    path('my_events/', user_views.my_events, name="my_events"),
]
