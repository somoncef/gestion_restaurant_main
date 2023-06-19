import datetime
from django.shortcuts import render
from .models import Reservation
from django.shortcuts import render, redirect
from django.contrib import messages
from user.views import default

def make_reservation(request):
    reserv = None  # Define a default value for 'reserv'

    if request.method == 'POST':
        # Check if a reservation already exists for the user
        if Reservation.objects.filter(user=request.user).exists():
            messages.error(request, 'You have already made a reservation.')
            return redirect(default)  

        # Proceed with creating the reservation
        dateres_str = request.POST.get('dater')
        dateres = datetime.datetime.strptime(dateres_str, "%Y/%m/%d %H:%M").date()
        nbr = request.POST.get('nbrpers')
        comm = request.POST.get('Commentaire')
        reservation_obj = Reservation.objects.create(user=request.user, nbrpersonne=nbr, date=dateres, commentaire=comm)
        reserv = Reservation.objects.all()
        print(reservation_obj)

    return render(request, 'reservation.html', {'reservation': reserv})
