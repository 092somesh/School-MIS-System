from django.shortcuts import render,redirect
from django.http import HttpResponse
from vege.seed import *
from .utils import send_email_to_client
# Create your views here.

def send_email(request):
    send_email_to_client()
    return redirect('/')
def home(request):
    peoples =[
        {'name' : 'abhijeet gupta' ,'age' : 26},
        {'name' : 'mohan' ,'age' : 24},
        {'name' : 'radhe' ,'age' : 12}, 
        {'name' : 'somesh' ,'age' : 23},
        {'name' : 'magan' ,'age' : 20},
    ]
    vegetables =['pumpkin','tomato','potato']
    return render(request , "home/index.html" ,context={ 'page':'djangotuto','peoples' : peoples, 'vegetables': vegetables })


def about(request):
    context={'page':'about'}
    return render(request , "home/about.html",context)

def contact(request):
    context={'page':'contact'}
    return render(request , "home/contact.html",context)
