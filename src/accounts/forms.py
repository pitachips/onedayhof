from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
import re
from django.core.validators import RegexValidator


def phone_validator(value):
    number = ''.join(re.findall(r'\d+', value))
    return RegexValidator(r'^01[016789]\d{7,8}$', message='번호를 입력해주세요')(number)


class SignupForm(UserCreationForm):
    is_agree = forms.BooleanField(label='약관동의', error_messages={
        'required' : '약관동의를 해주셔야 가입이 됩니다.',
        })
    school = forms.CharField()
    major = forms.CharField()

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        if commit:
            user.save()
            user.profile.school = self.cleaned_data['school']
            user.profile.major = self.cleaned_data['major']
            user.profile.is_store_owner = False
            user.profile.save()
        return user


class OwnerSignupForm(UserCreationForm):
    is_agree = forms.BooleanField(label='약관동의', error_messages={
        'required' : '약관동의를 해주셔야 가입이 됩니다.',
        })
    phone = forms.CharField(validators=[phone_validator])

    def save(self, commit=True):
        user = super(OwnerSignupForm, self).save(commit=False)
        if commit:
            user.save()
            user.profile.phone = self.cleaned_data['phone']
            user.profile.is_store_owner = True
            user.profile.save()
        return user
