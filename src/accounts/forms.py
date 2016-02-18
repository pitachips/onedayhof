from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
#from django.contrib.auth import get_user_model
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
        user.school = self.cleaned_data['school']
        user.major = self.cleaned_data['major']

        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "아이디를 입력하세요."
        self.fields['password1'].label = "패스워드를 입력하세요."
        self.fields['password2'].label = "패스워드를 다시 한 번 입력하세요."
        self.fields['school'].label = "소속학교를 정확하게 입력해주세요."
        self.fields['major'].label = "소속학과를 정확하게 입력해주세요"

class OwnerSignupForm(UserCreationForm):
    is_agree = forms.BooleanField(label='약관동의', error_messages={
        'required' : '약관동의를 해주셔야 가입이 됩니다.',
        })
    phone = forms.CharField(validators=[phone_validator])
    def save(self, commit=True):
        user = super(OwnerSignupForm, self).save(commit=False)
        user.phone = self.cleaned_data['phone']

        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(OwnerSignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "아이디를 입력하세요."
        self.fields['password1'].label = "패스워드를 입력하세요."
        self.fields['password2'].label = "패스워드를 다시 한 번 입력하세요."
        self.fields['phone'].label = "전화번호를 입력해주세요."
