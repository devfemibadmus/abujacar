from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from .models import Car
import random

def home(request):
    return render(request, 'home.html')

def get_car_brands_choices():
    return [
        ('Acura', 'Acura'),
        ('Aston Martin', 'Aston Martin'),
        ('Audi', 'Audi'),
        ('Bentley', 'Bentley'),
        ('BMW', 'BMW'),
        ('Bugatti', 'Bugatti'),
        ('Cadillac', 'Cadillac'),
        ('Chevrolet', 'Chevrolet'),
        ('Chrysler', 'Chrysler'),
        ('Dodge', 'Dodge'),
        ('Ferrari', 'Ferrari'),
        ('Ford', 'Ford'),
        ('Genesis', 'Genesis'),
        ('Gmc', 'GMC'),
        ('Honda', 'Honda'),
        ('Infiniti', 'Infiniti'),
        ('Jaguar', 'Jaguar'),
        ('Jeep', 'Jeep'),
        ('Kia', 'Kia'),
        ('Koenigsegg', 'Koenigsegg'),
        ('Lamborghini', 'Lamborghini'),
        ('Land Rover', 'Land Rover'),
        ('Lexus', 'Lexus'),
        ('Lincoln', 'Lincoln'),
        ('Maserati', 'Maserati'),
        ('Maybach', 'Maybach'),
        ('Mazda', 'Mazda'),
        ('Mclaren', 'McLaren'),
        ('Mercedes Benz', 'Mercedes Benz'),
        ('Mini', 'Mini'),
        ('Mitsubishi', 'Mitsubishi'),
        ('Nissan', 'Nissan'),
        ('Pagani', 'Pagani'),
        ('Peugeot', 'Peugeot'),
        ('Porsche', 'Porsche'),
        ('Rolls Royce', 'Rolls Royce'),
        ('Subaru', 'Subaru'),
        ('Suzuki', 'Suzuki'),
        ('Tesla', 'Tesla'),
        ('Toyota', 'Toyota'),
        ('Volkswagen', 'Volkswagen'),
    ]

def get_random_car_data():
    car_names = ["RX 350", "Civic", "Model S", "A4", "Corolla", "X5", "Mustang", "Camry", "GT-R", "911"]
    variants = ["Standard", "Luxury", "Sports", "Electric", "Hybrid", "Diesel"]
    conditions = ["Brand New", "Used", "Foreign Used"]
    colors = ["black", "blue", "red", "white", "silver", "green", "yellow", "grey"]
    types = ["SUV", "Sedan", "Hatchback", "Coupe", "Convertible", "Wagon", "Van", "Pickup", "Minivan", "Crossover"]
    years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
    mileages = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000]

    brands = get_car_brands_choices()

    car_data = []
    for brand_tuple in brands:
        brand = brand_tuple[1]
        car = {
            "id": 1,
            "name": random.choice(car_names),
            "year": random.choice(years),
            "mileage": random.choice(mileages),
            "color": random.choice(colors),
            "variant": random.choice(variants),
            "type": random.choice(types),
            "condition": random.choice(conditions),
            "brand": brand,
            "preview_image": "/cars/preview/bmw.jpg",
        }
        car_data.append(car)

    return car_data

def cars(request):
    query = request.GET.get('q')
    cars = Car.objects.filter(
        Q(name__icontains=query) |
        Q(type__icontains=query) |
        Q(year__icontains=query) |
        Q(brand__icontains=query) |
        Q(color__icontains=query) |
        Q(mileage__icontains=query) |
        Q(variant__icontains=query) |
        Q(condition__icontains=query)
    ) if query else Car.objects.all()
    cars = get_random_car_data()
    return render(request, 'cars.html', {'cars': cars})


def developer(request):
    return HttpResponseRedirect('https://www.instagram.com/devfemibadmus/')


