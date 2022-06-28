from django.urls import path
from . import views


urlpatterns = [
        path('',views.index),
        path('register', views.register),
        path('login', views.login),
        path('books', views.books),
        path('logout', views.logout),
        path('newBook', views.newBook),
        path('books/<int:_id>', views.bookPage),
        path('bookLiked/<int:_id>', views.bookLiked),
        path('del/<int:_id>', views.deleteBook),
        path('bookUnliked/<int:_id>', views.unlikeBook),
        path('update/<int:_id>',views.update),
        # path('proflie/<int:_id>' , views.profile),
]