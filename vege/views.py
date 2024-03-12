from django.shortcuts import render,redirect
from.models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.
@login_required(login_url="/login/")
def receipes(request):
    if request.method=="POST":
        data= request.POST
        
        receipe_name=data.get('receipe_name')
        receipe_description=data.get('receipe_description')
        receipe_image=request.FILES.get('receipe_image')
        
        Receipe.objects.create(
        receipe_name=receipe_name, 
        receipe_description=receipe_description,
        receipe_image=receipe_image,
        )
        
        return redirect('/receipes/')
    
    queryset= Receipe.objects.all()
    
    if request.GET.get('search'):
        queryset=queryset.filter(receipe_name__icontains=request.GET.get('search') )
    
    context= {'receipes': queryset}
    return render(request,'receipes/receipes.html',context) 

def delete_receipe(request,id):
    queryset=Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/receipes/')
def update_receipe(request,id):
    queryset=Receipe.objects.get(id=id)
    if request.method=="POST":
        data=request.post
        receipe_name=data.get('receipe_name')
        receipe_description=data.get('receipe_description')
        receipe_image=request.FILES.get('receipe_image')
        
        queryset.receipe_name=receipe_name
        queryset.receipe_description=receipe_description
        
        if receipe_image:
            queryset.receipe_image=receipe_image
            
        queryset.save()
        return redirect('/receipes/')   
    
    context= {'receipes': queryset}
    return render(request,'receipes/update_receipe.html',context) 

def login_page(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        if not User.objects.filter(username=username).exists():
            messages.error(request,'invaild user name')     
            return redirect('/login/')
    
        user = authenticate(username=username,password=password)
        if user is None:
            messages.error(request,'ivalid password')     
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/receipes/')   

    return render(request,'receipes/login.html')


def logout_page(request):
    logout(request)
    return redirect('/login/')      


        
def register_page(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request,'user name already taken')
            return redirect('/register/')
        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,    
        )
        user.set_password(password)
        user.save()
        messages.info(request,'account created')
            
        return redirect('/login/')
    return render(request,'receipes/register.html')

from django.db.models import Q,Sum
def get_students(request):
    queryset=Student.objects.all()
    
    if request.GET.get('search'):
        search=request.GET.get('search')
        queryset=queryset.filter(
        Q(student_name__icontains=search) |
        Q(department__department__icontains=search) |
        Q(student_id__student_id__icontains=search)   
        )
    
    paginator = Paginator(queryset, 20)  # Show 20 contacts per page.
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    return render(request,'report/student.html',{'queryset': page_obj})

from .seed import generate_report_card
def see_marks(request,student_id):
    queryset=SubjectMarks.objects.filter(student__student_id__student_id=student_id)
    total_marks=queryset.aggregate(total_marks=Sum ('marks'))
    return render(request,'report/see_marks.html',{'queryset': queryset, 'total_marks': total_marks})
