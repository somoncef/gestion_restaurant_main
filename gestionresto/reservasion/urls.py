from django.urls import path
from . import views




urlpatterns = [
    path('', views.make_reservation),
    path('removereservat/<int:id>', views.removereservation,name="removereservation"),

]