from django.shortcuts import render
from .models import User,UserProfile
from reservasion.models import Reservation

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


