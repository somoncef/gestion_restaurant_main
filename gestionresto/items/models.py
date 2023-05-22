from django.db import models

# Create your models here.

class item(models.Model):
    Categories_choices=(

        ("burger","burger"),
        ("pizza","pizza"),
        ("salade","salade"),
        ("tacos","tacos"),
        ("sandwich","sandwich"),
     
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories=models.CharField(max_length=100,choices=Categories_choices)

    def __str__(self):
        return self.name