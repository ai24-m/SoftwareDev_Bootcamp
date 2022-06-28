
from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('process_money', views.processMoney),
    path('reset', views.destroy)
]