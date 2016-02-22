from django.conf.urls import url, include
from django.contrib.auth.views import login
from accounts import views

urlpatterns = [
    url(r'^signupchoice/', views.signup_choice, name='signup_choice'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^owner_signup/', views.owner_signup, name='owner_signup'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^favorite_list/', views.favorite_list, name='favorite_list'),
    url(r'^mystore_list/', views.mystore_list, name='mystore_list'),
    url(r'', include('django.contrib.auth.urls')),
]