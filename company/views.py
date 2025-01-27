from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from .models import Car
import random

def home(request):
    return render(request, 'home.html')

def cars(request):
    query = request.GET.get('q')
    cars = Car.objects.filter(
        Q(name__icontains=query) |
        Q(type__icontains=query) |
        Q(brand__icontains=query) |
        Q(condition__icontains=query)
    ) if query else Car.objects.all()
    # cars = get_random_car_data()
    return render(request, 'cars.html', {'cars': cars})

def developer(request):
    return HttpResponseRedirect('https://www.instagram.com/devfemibadmus/')


