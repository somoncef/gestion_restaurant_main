from django.contrib import admin
from django.urls import path,include
from . import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('items/',include('items.urls')),
    path('login/', views.index),
    path('', views.home),
    path('signup/', views.signup),
   
]
