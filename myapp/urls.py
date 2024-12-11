from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index),
    path('userlogin/',views.userlogin,name='Login'),
    path('usersignup/',views.usersignup),
    path('perlogout/',views.perlogout),
    path('contectus/',views.contectus),
    path('profile/',views.profile,name="profile"),
    path('about/',views.about),
    path('otp/',views.otp,name='otp'),
    path('edituser/',views.edituser),
    path('node/',views.node,name="node"),
]
