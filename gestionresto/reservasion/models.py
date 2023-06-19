import django
from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Reservation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nbrpersonne = models.IntegerField()
    date=models.DateField(default=date.today)
    time = models.TimeField(default=django.utils.timezone.now)
    commentaire = models.TextField()

    def __str__(self):
        return f"Reservation for {self.user.username} on {self.date}"