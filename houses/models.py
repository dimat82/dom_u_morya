# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class House(models.Model):
    name = models.CharField(u'название', max_length=50)
    price = models.IntegerField(u'цена')
    description = models.TextField(u'описание')
    photo = models.ImageField(u'фотография', upload_to='houses/photo', default='', blank=True)

    class Meta:
        verbose_name = u'дом'
        verbose_name_plural = u'дома'
        ordering = ['price']


    def __str__(self):
        return self.name

