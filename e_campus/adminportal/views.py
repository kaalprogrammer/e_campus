from django.shortcuts import render
from django.views import View
from adminportal.models import *
from django.contrib.auth.models import AbstractUser


# Create your views here.

class HomeView(View):
    def get(self,request):
        return render(request, 'adminportal/index.html')

class About(View):
    def get(self,request):
        return render(request, 'adminportal/about.html')

class Gallery(View):
    def get(self,request):
        return render(request,'adminportal/gallery2.html')

class Contact(View):
    def get(self,request):
        return render(request,'adminportal/contact.html')

class Login(View):
    def get(self,request):
        return render(request,'adminportal/login.html')

#--------------How to do a multi user login in Django---------
class User(AbstractUser):
    is_admin = models.BooleanField('is_admin',default=False)
    is_faculty = models.BooleanField('is_faculty',default=False)
    is_student = models.BooleanField('is_student',default=False)