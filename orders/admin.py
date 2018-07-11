# -*- coding: utf-8 -*-
from django.contrib import admin
from orders.models import Order
# Register your models here.
class AdminOrder(admin.ModelAdmin):
    list_display = ['name','house','phone','date']

admin.site.register(Order,AdminOrder)

