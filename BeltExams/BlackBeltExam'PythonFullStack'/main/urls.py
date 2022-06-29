
from django.urls import path     
from . import views

urlpatterns = [
    path('',views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('wishes', views.dashboard),
    path('makeWish',views.newWish),
    path('new',views.wishAdd),
    path('state',views.state),
    path('grant/<_id>', views.grant),
    path('update/<int:_id>',views.update),
    path('edit/<int:_id>', views.editPage),
    path('delete/<_id>', views.delete),
    path('likes/<_id>',views.like),

]



