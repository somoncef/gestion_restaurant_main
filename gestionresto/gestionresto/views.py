
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from items import views as v
from django.http import JsonResponse
from django.contrib.auth import logout as django_logout
from user.models import UserProfile





def index(req):
    if req.method == 'POST':
        username=req.POST.get('username')
        passw=req.POST.get('pass')
        user=authenticate(username=username, password=passw)
        if user is not None:
            login(req, user)
            return redirect(v.default)
        else:
            messages.error(req,"bad username or password")
            return redirect('login')

        
        
    return render(req,'login.html',)
    



def signup(req):
    if req.method == 'POST':
        use = req.POST.get('username')
        lname = req.POST.get('lname')
        fname = req.POST.get('fname')
        email = req.POST.get('email')
        pass1 = req.POST.get('pass1')
        pass2 = req.POST.get('pass2')
        
        if not use:
            messages.error(req, "The given username must be set")
        elif pass1 != pass2:
            messages.error(req, "Passwords do not match")
        else:
            myuser = User.objects.create_user(use, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save() 
            myprofile = UserProfile.objects.create(myuser)
            myprofile.save()
            messages.success(req, "Successfully created")
            return redirect('login')
    
    return render(req, 'signup.html')

    

def home(respons):
    return render(respons,'home.html')

def about(respons):
    return render(respons,'about.html')

def logout(request):
    django_logout(request)
    return redirect('login')



