# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from houses.models import *
from django.views.generic.edit import CreateView,UpdateView
from orders.form import OrderForm
from houses.form import HousesListFilter

# Create your views here.


#class HouseDetailView(DetailView):
#    model = House
#    template_name = 'houses/house_detail.html'

def house_detail(request,house_id):
    houses = get_object_or_404(House,id=house_id)
    object_id = House.objects.filter(id=house_id).get()
    if request.method == 'POST':
        form = OrderForm(request.POST, initial={'house':object_id})
        if form.is_valid():
            form.save()
            return redirect('house_detail', house_id)
    else:
        form = OrderForm(initial={'house':object_id})
    return render(request, 'houses/house_detail.html', {'houses':houses, 'form':form,'object_id':object_id})

def houses_list(request):
    objects = House.objects.all()
    form = HousesListFilter(request.GET)
    if form.is_valid():
        if form.cleaned_data['min_price']:
            objects = House.objects.filter(price__gte=form.cleaned_data['min_price'])
        if form.cleaned_data['max_price']:
            objects = House.objects.filter(price__lte=form.cleaned_data['max_price'])
        if form.cleaned_data['ordering']:
            objects = objects.order_by(form.cleaned_data['ordering'])
    return render(request, 'houses/houses_list.html', {'objects':objects,'form':form})

#class HousesListView(ListView):
#    model = House
#    template_name = 'houses/houses_list.html'







