# -*- coding: utf-8 -*-
from django import forms
from orders.models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name','email','phone','house']



