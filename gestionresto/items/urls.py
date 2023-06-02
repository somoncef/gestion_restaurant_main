from django.contrib import admin
from django.urls import path,include
from . import views



urlpatterns = [
    path('', views.default),
    path('addtocart/', views.addtocart,name="addtocart"),
    path('cart/', views.cart,name="cart"),
    path('removefromcart/<int:id>', views.removefromcart,name="removefromcart"),
    path('addorremovequantity/<int:id>/<int:id>', views.addquantity,name="addorremovequantity"),
    path('removequantity/<int:id>/<int:id>', views.removequantity,name="removequantity"),

]
