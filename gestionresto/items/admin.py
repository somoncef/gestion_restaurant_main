from django.contrib import admin
from .models import item

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display=["name","price","categories"]

admin.site.register(item,ItemAdmin)

