from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    profiletypes=[

        ("user","user"),
        ("server","server"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='photos/profilepics/%y/%m/%d')
    address = models.CharField(max_length=200)
    typee=models.CharField(max_length=100,choices=profiletypes)

    def __str__(self):
        return self.user.username