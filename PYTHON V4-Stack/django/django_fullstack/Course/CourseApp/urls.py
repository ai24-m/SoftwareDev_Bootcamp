from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('newCourse', views.newCourse),
    path('delete/<int:_id>', views.delete),
    path('deletethis/<int:_id>', views.deletethis),

]