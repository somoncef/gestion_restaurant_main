from django.shortcuts import render
import requests



def index(respons):
    return render(respons,'login.html')

def signup(respons):
    return render(respons,'signup.html')

def home(respons):
    return render(respons,'base.html')

