from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('success/<int:num>', views.success),
    path('bears', views.one_method),
    # path('bears/<int:val>', views.another_method),
    # path('bears/<str:name>/poke', views.yet_another),
    path('bears/<int:id>/<str:color>', views.one_more),
    path('form', views.form_handler),
    path('bears', views.form_handler),
]