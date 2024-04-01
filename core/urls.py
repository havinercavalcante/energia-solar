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
>>>>>>> ec2fe25 (Add files via upload)
