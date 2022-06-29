from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('shows',views.shows),
    path('shows/new',views.addPage),
    path('shows/create',views.newShow), 
    path('shows/<_id>',views.show),
    path('shows/<_id>/edit',views.showEdit),
    path('shows/<_id>/update',views.showUpdate),
    path('shows/<_id>/destroy',views.showDestory),

]
