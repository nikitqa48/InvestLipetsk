from django.conf import settings
from django.db import models
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Profile, Statement, Organisation, Connection, Message
from captcha.fields import CaptchaField
class Profile_form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['second_name',"phone","last_name"]


class Organisation_form(forms.ModelForm):
    class Meta:
        model = Organisation
        fields = ["organisation_name", "industry", "contacts"]


class Statement_form(forms.ModelForm):
    """ФОРМА ЗАЯВКИ"""
    class Meta:   
        model = Statement
        fields = ["project_name", "industry", "cost", "square", "work", "description"]
        widgets={
                   "project_name":forms.TextInput(attrs={'placeholder':'','name':'Name','class':'', 'required':'required'}),
                   "industry":forms.TextInput(attrs={'placeholder':'','name':'Name','class':'', 'required':'required'}),
                   "cost":forms.TextInput(attrs={'placeholder':'','name':'Name','class':'', 'required':'required'}),
                   "work":forms.TextInput(attrs={'placeholder':'','name':'Name','class':'', 'required':'required'}),
                   "square":forms.TextInput(attrs={'placeholder':'','name':'Name','class':'', 'required':'required'}),
            }  
class Data_form(forms.ModelForm):
    """форма даты исполнения заявки"""
    class Meta:
        model = Statement
        fields = ['time']
        widgets = {
            'time':forms.TextInput(attrs={'required':'required', 'class':'time','type':'date'})
        }

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    captcha = CaptchaField()
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
    """ФОРМА СВЯЗИ НА ВСЕХ СТРАНИЦАХ"""
    captcha = CaptchaField()
    class Meta:
        model = Connection
        fields = ['phone', 'first_name', 'second_name', 'organisation', 'email', 'last_name']
        widgets={
                   "phone":forms.TextInput(attrs={'placeholder':'','name':'Name','class':'input-first', 'required':'required', 'type':'tel'}),
                   "email":forms.TextInput(attrs={'placeholder':'','name':'Name','class':'input-first', 'required':'required', 'type':'email'}),
                   "first_name":forms.TextInput(attrs={'placeholder':'','name':'Name','class':'input-name', 'required':'required'}),
                   "second_name":forms.TextInput(attrs={'placeholder':'','name':'Name','class':'input-name', 'required':'required'}),
                   "organisation":forms.TextInput(attrs={'placeholder':'','name':'Name','class':'input-class_name'}),
                   'last_name':forms.TextInput(attrs={'placeholder':'','name':'Name','class':'input-otch'})
            }  


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text']

