from django.shortcuts import render, redirect
from accounts.forms import SignupForm, OwnerSignupForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def signup_choice(request):
    return render(request, 'accounts/signup_choice.html')


#학생회원 가입
def signup(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                user = form.save()
                authenticated_user = authenticate(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password1'])
                login(request, authenticated_user)
            messages.success(request, '환영합니다. ;)')
            return redirect('/')
        else:
            form = SignupForm()
        return render(request, 'accounts/signup.html', {'form': form, })
    else:
        messages.info(request, "잘못된 접근입니다.")
        return redirect('index')


# 업주회원 가입
def owner_signup(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            form = OwnerSignupForm(request.POST)

            if form.is_valid():
                form.save()
                username=form.cleaned_data['username']
                user =User.objects.get(username=username)
                authenticated_user = authenticate(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password1'])
                login(request, authenticated_user)
                messages.info(request, '환영합니다. 업체를 등록해주세요.')
                return redirect('store_new')
        else:
            form = OwnerSignupForm()
        return render(request, 'accounts/owner_signup.html', {'form': form, })
    else:
        messages.info(request, "잘못된 접근입니다.")
        return redirect('index')


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

