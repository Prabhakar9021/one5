import email
from email import message
from re import template
import re
from telnetlib import AUTHENTICATION
from urllib.request import Request
from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from django.template.loader import get_template 
from .models import table
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    #table1=table.objects.all()
    return render(request,'index.html')

#def contact(request):
    if request.method=="POST":
        uname=request.POST['username']
        upass=request.POST['password']
        User=authenticate(request,username=uname,password=upass)
        if User is not None:
            login(request,User)
            return HttpResponseRedirect('profile')
        else:
            return HttpResponse("invalid credintal")
    return render(request,'page2.html')

#def register(request):
    if request.method=="POST":
        form1=UserCreationForm(request.POST)
        if form1.is_valid():
            form1.save()
            
    else:
        form1=UserCreationForm() 
    return render(request,'register.html',{'form2':form1})
   
#def profile(request):
    if  request.user.is_authenticated:
        return render(request,'profile.html', {'name':request.user})
    else:
        return HttpResponseRedirect('contact')

#def logut(request):
    logout(request)
    return HttpResponseRedirect('contact')
        
               
    
     
    
       
    
    

#adding records to db



