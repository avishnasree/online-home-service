from django.contrib import admin

# Register your models here.
from homeserviceapp import models

admin.site.register(models.workerpage)
admin.site.register(models.userpage)
