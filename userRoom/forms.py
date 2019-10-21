from django.conf import settings
from django.db import models
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Profile, Statement, Organisation

class Profile_form (forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["email", "phone", "profile"]

class Organisation_form (forms.ModelForm):
    class Meta:
        model = Organisation
        fields = ["organisation_name", "industry","contacts"]
        
class Statement_form (forms.ModelForm):
    class Meta:
        model = Statement
        fields = ["project_name", "industry", "data_send", "cost", "square", "work", "company", "description"]

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)