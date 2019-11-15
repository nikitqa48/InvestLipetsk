from django.conf import settings
from django.db import models
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Profile, Statement, Organisation, Connection
# 

class Profile_form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['second_name',"phone"]


class Organisation_form(forms.ModelForm):
    class Meta:
        model = Organisation
        fields = ["organisation_name", "industry", "contacts"]


class Statement_form(forms.ModelForm):
    class Meta:
        model = Statement
        fields = ["project_name", "industry", "cost", "square", "work", "description"]


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email')
        labels = ({'username': 'Логин', 'last_name': 'Отчество (Если есть)'})

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']

class ConnectionForm(forms.ModelForm):
    class Meta:
        model = Connection
        fields = ['phone', 'first_name', 'second_name', 'organisation', 'email', 'last_name']