from django.db import models
from django.contrib.auth.models import User
from reservasion.models import Reservation

class UserProfile(models.Model):
    profiletypes=[

        ("user","user"),
        ("server","server"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='photos/profilepics/%y/%m/%d')
    phone =models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    typee=models.CharField(max_length=100,choices=profiletypes) 
    reservation_count = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
    
    def calculate_reservation_count(self):
        return Reservation.objects.filter(user=self.user).count()

    def save(self, *args, **kwargs):
        self.reservation_count = self.calculate_reservation_count()
        super().save(*args, **kwargs)