from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cars', views.cars, name='cars'),
    path('developer', views.developer, name='developer'),
]
