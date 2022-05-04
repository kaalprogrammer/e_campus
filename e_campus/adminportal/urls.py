
from django.urls import path,include

from . import views
from .views import *
from generic.views import BaseCourseView,BaseCreateView,BaseDeleteView,BaseUpdateView,ThanksUpdateView,BaseUserCreateView,BaseUserView
urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('about/',views.About.as_view(),name='about'),
    path('gallery/',views.Gallery.as_view(),name='gallery'),
    path('contact/',views.Contact.as_view(),name='contact'),
    path('login/',views.Login.as_view(),name='login'),

 
    path('course_create/',BaseCreateView.as_view(), name ='course_create'),
    path('update/<int:pk>',BaseUpdateView.as_view(), name ='course_update'),
    path('delete/<int:pk>',BaseDeleteView.as_view(), name ='course_delete'),
    path('course_view/',BaseCourseView.as_view(), name ='course_view'),
    path('thanks/',ThanksUpdateView.as_view(), name ='thanks'),
    # path('courseview/',views.courseview, name='course_view'),
    path('user_create/',BaseUserCreateView.as_view(), name ='user_create'),
    path('user_view/',BaseUserView.as_view(), name ='user_view'),
]