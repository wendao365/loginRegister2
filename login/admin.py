from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.User)#把models.User注册到后台去