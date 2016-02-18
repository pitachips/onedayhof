from django.conf.urls import url
from django.contrib.auth.views import login
from accounts import views

urlpatterns = [
    url(r'^signupchoice/', views.signupchoice, name='signupchoice'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^ownersignup/', views.ownersignup, name='ownersignup'),
    ]