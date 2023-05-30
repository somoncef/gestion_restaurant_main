from django.contrib import admin
from django.urls import path,include
from . import views



urlpatterns = [
    path('', views.default),
    path('addtocart/', views.addtocart,name="addtocart"),
]
