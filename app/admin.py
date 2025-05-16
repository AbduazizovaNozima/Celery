from django.contrib import admin
from .models import *


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'phone')
