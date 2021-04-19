from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("process_money", views.process_money),
    path("clear", views.clear),
    path("game", views.game),
    path("set_rules", views.set_rules),
]