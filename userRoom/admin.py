from django.contrib import admin
from .models import Profile, Organisation, Statement
# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'phone', 'id']

@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ['contacts', 'organisation_name', 'industry', "id"]

@admin.register(Statement)
class Statement(admin.ModelAdmin):
    list_display = ['statement_user', 'project_name', 'description', 'industry', 'cost', 'square', 'work', 'company']

