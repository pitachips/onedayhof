from django.conf.urls import url
from django.contrib.auth.views import login
from accounts import views

urlpatterns = [
    url(r'^signupchoice/', views.signup_choice, name='signup_choice'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^owner_signup/', views.owner_signup, name='owner_signup'),
    ]