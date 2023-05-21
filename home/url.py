from unicodedata import name
from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    #path('contact',views.contact,name='contact'),
    #path('register',views.register,name='register'),
    #path('profile',views.profile,name='profile'),
    #path('logout',views.logut,name='logout')
    
]
