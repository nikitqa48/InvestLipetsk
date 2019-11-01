from django.contrib import admin
from .models import Profile, Organisation, Statement, Manager
# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'phone', 'id']

@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ['contacts', 'organisation_name', 'industry', "id"]

@admin.register(Statement)
class Statement(admin.ModelAdmin):
    list_display = ['project_name', 'description', 'industry', 'cost', 'square', 'work','data_send']

@admin.register(Manager)
class Statement(admin.ModelAdmin):
    list_display = ['manager', 'zayavka','data_send']

