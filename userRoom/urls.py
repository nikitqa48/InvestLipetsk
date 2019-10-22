from django.urls import path
from userRoom.views import *
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # path('', views.new_profile, name='new_profile'),
    path('profile_view/', new_profile, name='profile_view'),
    path('profile_edit/<int:pk>', edit_profile, name='profile'),
    path('statement/', new_statement, name='statement'),
    path('organisation_view/', new_organisation, name='organisation_view'),
    path('organisation_edit/<int:pk>',edit_organisation, name='edit_organisation')
    # url(r'^login/$', user_login, name='login'),
    #

]
