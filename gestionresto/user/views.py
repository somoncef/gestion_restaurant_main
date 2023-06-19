from django.shortcuts import redirect, render
from .models import User,UserProfile
from reservasion.models import Reservation
from .forms import ImageForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import TemplateView, CreateView
from django.core.exceptions import ObjectDoesNotExist



@login_required

def default(request):
    profile = UserProfile.objects.get(user=request.user)
    try:
        reservation = Reservation.objects.get(user=request.user)
        if reservation is not None:
            return render(request, 'profile.html', {'profile': profile, 'reservation': reservation})
    except Reservation.DoesNotExist:
        pass

    return render(request, 'profile.html', {'profile': profile})

@login_required
def profileupdate(request):
    profile = UserProfile.objects.get(user=request.user)
    reservation = Reservation.objects.get(user=request.user)
    return render(request, 'profile-update.html', {'profile': profile, "reservation": reservation})

def index(request):
    if request.method == "POST":
        form=ImageForm(data=request.POST,files=request.FILES)
    if form.is_valid():
        form.save()
        obj=form.instance
        return render(request,"profile.html",{"obj":obj})
    else:
        form=ImageForm()
    Userp=UserProfile.objects.all()
    return render(request,"profile.html",{"Userp":Userp,"form":form})

@login_required
def update(req):    
    if req.method == 'POST':
        lname = req.POST.get('last_name')
        fname = req.POST.get('first_name')
        email = req.POST.get('email')
        phone = req.POST.get('phone')
        address = req.POST.get('address')
    
    
        myuser = UserProfile.objects.get(user=req.user)
        myuser.user.first_name = fname
        myuser.user.last_name = lname
        myuser.user.email = email
        myuser.phone = phone
        myuser.address = address
        myuser.save()

        return redirect('profile.html')
     
    return render(req, 'profile.html')