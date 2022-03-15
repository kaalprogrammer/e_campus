from django.shortcuts import render
from django.views import View
from adminportal.models import *
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

