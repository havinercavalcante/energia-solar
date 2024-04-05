<<<<<<< HEAD
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('calculator.urls')),
]
=======
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('calculator.urls')),
]
>>>>>>> ec2fe25c217fc0007165b8fd2c342f4f5c9d1f56
