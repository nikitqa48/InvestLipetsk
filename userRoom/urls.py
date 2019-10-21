from django.urls import path
from userRoom.views import *
from django.conf.urls import include, url
from django.contrib import admin
urlpatterns = [
    #path('', views.new_profile, name='new_profile'),
    path('organisation/', new_organisation, name = 'organisation'),
    path('profile_view/', new_profile, name= 'profile_view'),
    path('profile_edit/<int:pk>', Profile_new.as_view(), name= 'profile'),
    path('statement/', new_statement, name='statement'),
    url(r'^login/$', user_login, name='login'),
    
    
]