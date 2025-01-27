from .models import Car
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        year = cleaned_data.get('year')
        color = cleaned_data.get('color')
        variant = cleaned_data.get('variant')
        car_type = cleaned_data.get('type')
        condition = cleaned_data.get('condition')
        brand = cleaned_data.get('brand')
        car = Car.objects.filter(name=name, year=year, color=color, variant=variant, type=car_type, condition=condition, brand=brand)
        if self.instance.pk and car.exclude(id=self.instance.pk).exists():
            self.add_error(None, 'A car with these details already exists.')
        if not self.instance.pk and car.exists():
            self.add_error(None, 'A car with these details already exists.')
        return cleaned_data
    
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'type', 'condition', 'color')
    list_filter = ('type', 'condition', 'year')
    search_fields = ('name', 'year', 'brand')
    form = CarForm
    fieldsets = (
        ("Car Details", {
            'fields': ('name', 'year', 'amount', 'mileage', 'postUrl', 'preview_image')
        }),
        ("Car Information (used on the website when searching for a car)", {
            'fields': ('variant', 'color', 'type', 'brand')
        }),
    )
    

admin.site.unregister(Group)


