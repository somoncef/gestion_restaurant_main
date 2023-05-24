
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from items import views as v




def index(req):
    if req.method == 'POST':
        username=req.POST['username']
        passw=req.POST['pass']
        user=authenticate(username=username, password=passw)
        if user is not None:
            login(req, user)
        else:
            messages.error(req,"bad username or password")

        return redirect(v.default)
        
    return render(req,'login.html',)
    

def signup(req):
    if req.method == 'POST':
        use=req.POST.get('username')
        lname=req.POST.get('lname')
        fname=req.POST.get('fname')
        email=req.POST.get('email')
        pass1=req.POST.get('pass1')
        pass2=req.POST.get('pass2')
        
        if pass1!=pass2:
            messages.error(req ,"passwords do not match")
           
        myuser=User.objects.create_user(use,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save() 
        messages.success(req , "Successfully created")
        return redirect('login.html')
            
    return render(req,'signup.html')

def home(respons):
    return render(respons,'base.html')

