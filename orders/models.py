# -*- coding: utf-8 -*-
from django.db import models
from houses.models import House
# Create your models here.
class Order(models.Model):
    house = models.ForeignKey(House, verbose_name=u'дом',on_delete='')
    name = models.CharField(u'имя',max_length=100)
    email = models.EmailField()
    phone = models.CharField(u'телефон',max_length=100)
    date = models.DateTimeField(u'дата создания',auto_now_add=True)



