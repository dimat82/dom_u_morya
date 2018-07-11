# -*- coding: utf-8 -*-
from django import forms

class HousesListFilter(forms.Form):
    min_price = forms.IntegerField(label='от',required=False)
    max_price = forms.IntegerField(label='до',required=False)
    ordering = forms.ChoiceField(label='сортировка',required=False,choices=[
        ['name',u'по имени'],
        ['price',u'дешевые сверху'],
        ['-price',u'дорогие сверху']
    ])

