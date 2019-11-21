from django.contrib import admin
from .models import Profile, Organisation, Statement, Manager, News, Connection
# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'phone', 'id']

@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ['contacts', 'organisation_name', 'industry', "id"]

@admin.register(Statement)
class Statement(admin.ModelAdmin):
    list_display = ['project_name', 'description', 'industry', 'cost', 'square', 'work','data_send','id', 'time','status']

@admin.register(Manager)
class Statement(admin.ModelAdmin):
    list_display = ['manager', 'zayavka','data_send']

@admin.register(News)
class newsAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'news_data', 'news_header', 'news_text']

@admin.register(Connection)
class connectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone', 'first_name', 'second_name', 'last_name', 'email','organisation']