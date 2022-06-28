from django.urls import path   

from . import views
urlpatterns = [
    path('', views.index),
    path('AddBook',views.addBook),
    path('books/<_id>/',views.InfoBook),
    path('deleteBook/<_idBook>/',views.delete),
    path('AddAuthor_Book/<int:_id>/', views.addAuthor_Book),
    path('authors',views.author),
    path('AddAuthor', views.addAuthor),
    path('authors/<_id>/',views.InfoAuthor),
    path('delete_author/<_idAuthor>',views.delete_author),
    path('AddBook_Author/<int:_id>/', views.addBook_Author),
]