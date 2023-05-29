from django.contrib import admin
from .models import item,cartitems,Cart


# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display=["name","price","categories"]


class cartAdmin(admin.ModelAdmin):
    list_display=["id","complete","user"]

class cartitemsAdmin(admin.ModelAdmin):
    list_display=["product","cart","quantity"]

admin.site.register(item,ItemAdmin)
admin.site.register(cartitems,cartitemsAdmin)
admin.site.register(Cart,cartAdmin)



