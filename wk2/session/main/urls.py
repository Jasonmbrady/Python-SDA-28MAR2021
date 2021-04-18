from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("get_user", views.get_user),
    path("display_user", views.display_user),
    path("make_box", views.make_box),
    path("clear", views.clear),
]