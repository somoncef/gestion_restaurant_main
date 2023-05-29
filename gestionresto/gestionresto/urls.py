from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from . import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('items/',include('items.urls'),name="items"),
    path('login/', views.index,name="login"),
    path('', views.home,name="index"),
    path('signup/', views.signup),
    path('about/', views.about),
    path('addtocart/', views.addtocart,name="addtocart"),

   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
