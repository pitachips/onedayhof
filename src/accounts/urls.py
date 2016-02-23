from django.conf.urls import url, include
from django.contrib.auth.views import login
from django.contrib.auth.views import password_change

from . import views
from .forms import PassChangeForm, LoginForm


urlpatterns = [
    url(r'^signupchoice/', views.signup_choice, name='signup_choice'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^owner_signup/', views.owner_signup, name='owner_signup'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^favorite_list/', views.favorite_list, name='favorite_list'),
    url(r'^mystore_list/', views.mystore_list, name='mystore_list'),
    url(r'^access_terms/', views.access_terms, name='access_terms'),
    url(r'^login/$', login, kwargs={'authentication_form': LoginForm, }, name="login"),
    url(r'^password_change/$', password_change, kwargs={'password_change_form': PassChangeForm, 'template_name':'registration/pass_change_form.html', }, name="password_change"),
    url(r'', include('django.contrib.auth.urls')),
]