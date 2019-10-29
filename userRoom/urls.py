from django.urls import path
from userRoom.views import *
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    path('registration', register, name="register"),
    path('', head_page, name= 'container'),
    path('logout', logout_view, name='logout'),
    path('private/<int:pk>', private_area, name = 'private'),
    path('profile_view/', new_profile, name='profile_view'),
    path('profile_edit/<int:pk>', edit_profile, name='profile'),
    path('statement_view/', new_statement, name="statement_view"),
    path('statement_edit/<int:pk>', edit_statement, name='statement'),
    path('organisation_view/', new_organisation, name='organisation_view'),
    path('organisation_edit/<int:pk>',edit_organisation, name='edit_organisation'),
    path('login/', user_login,name="login")
    # url(r'^login/$', user_login, name='login'),
]
