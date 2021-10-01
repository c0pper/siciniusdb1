from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("user-subs/", views.user_subs, name="user-subs"),
]
