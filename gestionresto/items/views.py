import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import item,Cart
from .models import cartitems as Cartitem



# Create your views here.
def default(request):
    def get_all_categories():
        categories = item.Categories_choices
        return [category[0] for category in categories]
    items = item.objects.all()
    cat=get_all_categories()
    return render(request, 'items.html', {'items': items,'cat': cat})

def addtocart(req):
    data=json.loads(req.body)
    product_id = data["id"]
    product=item.objects.get(id=product_id)
    if req.user.is_authenticated:
        cart, created=Cart.objects.get_or_create(user=req.user,complete=False)
        cartitem, created=Cartitem.objects.get_or_create(cart=cart,product=product)
        cartitem.quantity +=1
        cartitem.save()

        print(cartitem)
    return JsonResponse("it is working",safe=False)