from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('newdojo', views.newDojo),
    path('newninja', views.newNinja),
    path('<_id>', views.delete),
]