from django.contrib import admin
from django.urls import path, include
from userRoom import views
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('userRoom.urls')),
    path('profile/', include('userRoom.urls')),
]
