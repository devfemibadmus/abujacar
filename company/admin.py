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
    list_display = ('name', 'brand', 'year', 'color', 'car_mileage', 'car_amount')
    list_filter = ('type', 'condition', 'brand')
    search_fields = ('name',)
    form = CarForm
    def car_amount(self, obj):
        return f'₦{obj.amount:,.0f}'
    def car_mileage(self, obj):
        if obj.mileage >= 1_000_000:
            return f'{obj.mileage // 1_000_000}m miles'
        elif obj.mileage >= 1_000:
            return f'{obj.mileage // 1_000}k miles'
        return f"{obj.mileage} miles"
    fieldsets = (
        ("Car Details", {
            'fields': ('brand', 'name', 'year', 'mileage', 'postUrl', 'preview_image')
        }),
        ("Car Information (used on the website when searching for a car)", {
            'fields': ('amount', 'color', 'type', 'condition')
        }),
    )
    

admin.site.unregister(Group)
admin.site.site_header = "Abuja Car"


