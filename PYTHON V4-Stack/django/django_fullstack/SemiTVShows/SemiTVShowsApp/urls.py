from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('shows',views.shows),
    path('shows/new',views.show_new, name='new_show'),
    path('shows/create',views.create_show),
    path('shows/<_id>',views.show),
    path('shows/<_id>/edit',views.show_edit),
    path('shows/<_id>/update',views.show_update),
    path('shows/<_id>/destroy',views.show_destory),

]
