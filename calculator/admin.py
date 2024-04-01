<<<<<<< HEAD
from django.contrib import admin
from .models import Consumer

class ConsumerAdmin(admin.ModelAdmin):
    list_display = ('name', 'document', 'city', 'state', 'consumption', 'distributor_tax')
    search_fields = ('name', 'document', 'city', 'state')

admin.site.register(Consumer, ConsumerAdmin)
=======
from django.contrib import admin

from . import models

admin.site.register(models.Consumer)
>>>>>>> ec2fe25 (Add files via upload)
