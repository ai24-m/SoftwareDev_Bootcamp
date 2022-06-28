from django.urls import path     
from . import views
urlpatterns = [
    # path('', views.root),
    path('', views.index),
    path('show', views.show),
    path('newgame', views.newgame),
]
