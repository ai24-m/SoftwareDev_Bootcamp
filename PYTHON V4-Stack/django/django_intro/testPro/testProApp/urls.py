
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('root', views.root),
    path('', views.destroy)

    # path('', views.index),
    # path('processmoney', views.processMoney),
    # path('destroy', views.destroy)
]



# from django.urls import path     
# from . import views

# urlpatterns = [
#     path('', views.root),
#     path('process_money',views.process),
#     path('reset', views.reset),
# ]