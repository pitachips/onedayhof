from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
import re
from django.core.validators import RegexValidator

from .models import Profile
from django.utils.translation import ugettext_lazy as _

def phone_validator(value):
    number = ''.join(re.findall(r'\d+', value))
    return RegexValidator(r'^01[016789]\d{7,8}$', message='번호를 입력해주세요')(number)


class SignupForm(UserCreationForm):
    username = forms.CharField(label='아이디')
    password1 = forms.CharField(label='비밀번호', widget=forms.PasswordInput)
    password2 = forms.CharField(label='비밀번호 확인', widget=forms.PasswordInput)
    school = forms.CharField(label='대학이름')
    major = forms.CharField(label='소속', widget=forms.TextInput(attrs={'placeholder': '본인이 속한 단과대학이나 동아리 이름을 적어주세요.'}), )
    is_agree = forms.BooleanField(label='약관동의', error_messages={
        'required' : '약관동의를 해주셔야 가입이 됩니다.',
    })

    error_messages = {
        'password_mismatch': _("비밀번호가 일치하지 않습니다."),
    }

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        if commit:
            user.save()
            user.profile.school = self.cleaned_data['school']
            user.profile.major = self.cleaned_data['major']
            user.profile.is_store_owner = False
            user.profile.save()
        return user


class UpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('school', 'major', )



class OwnerSignupForm(UserCreationForm):
    username = forms.CharField(label='아이디')
    password1 = forms.CharField(label='비밀번호', widget=forms.PasswordInput)
    password2 = forms.CharField(label='비밀번호 확인', widget=forms.PasswordInput)
    phone = forms.CharField(label='휴대폰 번호', widget=forms.TextInput(attrs={'placeholder': 'ex) 010-1234-5678'}), validators=[phone_validator])
    is_agree = forms.BooleanField(label='약관동의', error_messages={
        'required' : '약관동의를 해주셔야 가입이 됩니다.',
    })

    error_messages = {
        'password_mismatch': _("비밀번호가 일치하지 않습니다."),
    }

    def save(self, commit=True):
        user = super(OwnerSignupForm, self).save(commit=False)
        if commit:
            user.save()
            user.profile.phone = self.cleaned_data['phone']
            user.profile.is_store_owner = True
            user.profile.save()
        return user

class OwnerUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('phone', )
