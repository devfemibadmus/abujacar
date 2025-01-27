from django.db import models

class Car(models.Model):
    CAR_TYPE_CHOICES = [
        ('SUV', 'SUV'),
        ('Sedan', 'Sedan'),
        ('Hatchback', 'Hatchback'),
        ('Coupe', 'Coupe'),
        ('Convertible', 'Convertible'),
        ('Wagon', 'Wagon'),
        ('Van', 'Van'),
        ('Pickup', 'Pickup'),
        ('Minivan', 'Minivan'),
        ('Crossover', 'Crossover'),
    ]
    CAR_CONDITION_CHOICES = [
        ('Brand New', 'Brand New'),
        ('Used', 'Used'),
        ('Foreign Used', 'Foreign Used'),
    ]
    CAR_BRANDS_CHOICES = [
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
    CAR_COLORS_CHOICES = [
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('Black', 'Black'),
        ('White', 'White'),
        ('Silver', 'Silver'),
        ('Green', 'Green'),
        ('Yellow', 'Yellow'),
        ('Orange', 'Grey'),
        ('orange', 'Orange'),
        ('Brown', 'Brown'),
    ]
    name = models.CharField(max_length=9)
    postUrl = models.URLField(max_length=200)
    year = models.PositiveIntegerField()
    mileage = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    color = models.CharField(max_length=20, choices=CAR_COLORS_CHOICES)
    type = models.CharField(max_length=20, choices=CAR_TYPE_CHOICES)
    condition = models.CharField(max_length=20, choices=CAR_CONDITION_CHOICES)
    brand = models.CharField(max_length=20, choices=CAR_BRANDS_CHOICES)
    preview_image = models.ImageField(upload_to="preview/")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand} - {self.year}"

    class Meta:
        ordering = ['-updated_at']
        verbose_name = "Car"
        verbose_name_plural = "Cars"

