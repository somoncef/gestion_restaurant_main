from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class item(models.Model):
    Categories_choices=[

        ("burger","burger"),
        ("pizza","pizza"),
        ("salade","salade"),
        ("tacos","tacos"),
        ("sandwich","sandwich"),
     
    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories=models.CharField(max_length=100,choices=Categories_choices)

    def __str__(self):
        return self.name
    
    
class Cart(models.Model):
    id=models.UUIDField(default=uuid.uuid4,primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    complete=models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    @property
    def total_price(self):
        cartitems = self.cartitem.all()
        total = sum([item.price for item in cartitems])
        return total
    
    
      
    @property
    def num_of_items(self):
        cartitems = self.cartitem.all()
        quantity = sum([item.quantity for item in cartitems])
        return quantity
    

    
    
class cartitems(models.Model):
    product=models.ForeignKey(item,on_delete=models.CASCADE,related_name="items") 
    cart= models.ForeignKey(Cart ,on_delete=models.CASCADE,related_name="cartitem")  
    quantity=models.IntegerField(default=0)  
    

    def __str__(self):
        return str(self.product.name)  


    @property
    def price(self):
        return self.product.price*self.quantity     
    

    
