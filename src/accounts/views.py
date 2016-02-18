from django.shortcuts import render, redirect
from accounts.forms import SignupForm,OwnerSignupForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages


# Create your views here.
def signupchoice(request):
    return render(request, 'accounts/signupchoice.html')

def signup(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            form = SignupForm(
                request.POST,
                initial={"school": "소속학교", "major": "소속학과/동아리"})

            if form.is_valid():
                form.save()
                username=form.cleaned_data['username']
                user =User.objects.get(username=username)
                authenticated_user = authenticate(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password1'])
                login(request, authenticated_user)
                messages.info(request, '환영합니다')
                return redirect('/')
        else:
            form = SignupForm()
        return render(request, 'accounts/signup.html', {'form': form, })
    else:
        messages.info(request, "잘못된 접근입니다.")
        return redirect('hof:index')

def ownersignup(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            form = OwnerSignupForm(
                request.POST)

            if form.is_valid():
                form.save()
                username=form.cleaned_data['username']
                user =User.objects.get(username=username)
                authenticated_user = authenticate(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password1'])
                login(request, authenticated_user)
                messages.info(request, '환영합니다')
                return redirect('/')
        else:
            form = OwnerSignupForm()
        return render(request, 'accounts/ownersignup.html', {'form': form, })
    else:
        messages.info(request, "잘못된 접근입니다.")
        return redirect('hof:index')
