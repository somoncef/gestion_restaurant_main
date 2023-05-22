from django.shortcuts import render
from .models import item


# Create your views here.
def default(request):
    items = item.objects.all()
    return render(request, 'items.html', {'items': items})d

