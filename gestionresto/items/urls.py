from django.contrib import admin
from django.urls import path,include
from . import views



urlpatterns = [
    path('', views.default),
    path('addtocart/', views.addtocart,name="addtocart"),
    path('cart/', views.cart,name="cart"),
    path('removefromcart/<int:id>', views.removefromcart,name="removefromcart"),
    path('addquantity/<int:id>/<int:quantity>', views.addquantity,name="addquantity"),
    path('removequantity/<int:id>/<int:quantity>', views.removequantity,name="removequantity"),

]
