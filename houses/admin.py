# -*- coding: utf-8 -*-
from django.contrib import admin
from houses.models import *
# Register your models here.


class AdminHouse(admin.ModelAdmin):
    list_display = ['name', 'price']

admin.site.register(House, AdminHouse)
