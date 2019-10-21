from django.contrib import admin
from .models import Profile, Organisation, Statement
# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['profile', 'email', 'phone', 'id']

