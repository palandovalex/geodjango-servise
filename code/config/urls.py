from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/users/', include('users.urls')),
    path('api/v1/countries/', include('countries.urls')),
    path('api/v1/cities/', include('cities.urls')),
    path('admin/', admin.site.urls),
]
