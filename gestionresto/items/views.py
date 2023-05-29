from django.shortcuts import render
from .models import item



# Create your views here.
def default(request):
    def get_all_categories():
        categories = item.Categories_choices
        return [category[0] for category in categories]
    items = item.objects.all()
    cat=get_all_categories()
    return render(request, 'items.html', {'items': items,'cat': cat})

