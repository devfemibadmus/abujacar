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
    CAR_VARIANT_CHOICES = [
        ('Standard', 'Standard'),
        ('Luxury', 'Luxury'),
        ('Sports', 'Sports'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid'),
        ('Diesel', 'Diesel'),
    ]
    CAR_CONDITION_CHOICES = [
        ('NEW', 'Brand New'),
        ('USED', 'Used'),
        ('FOREIGN_USED', 'Foreign Used'),
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
    name = models.CharField(max_length=9, default="RX 350")
    postUrl = models.CharField(max_length=150, default="https://www.instagram.com/abujacar/")
    year = models.PositiveIntegerField(default=2010)
    mileage = models.PositiveIntegerField(default=10000)
    color = models.CharField(max_length=20, choices=CAR_COLORS_CHOICES, default='black')
    variant = models.CharField(max_length=20, choices=CAR_VARIANT_CHOICES, default='Luxury')
    type = models.CharField(max_length=20, choices=CAR_TYPE_CHOICES, default='SUV')
    condition = models.CharField(max_length=20, choices=CAR_CONDITION_CHOICES, default='USED')
    brand = models.CharField(max_length=20, choices=CAR_BRANDS_CHOICES, default='lexus')
    preview_image = models.ImageField(upload_to="preview/")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand} - {self.year}"

    class Meta:
        ordering = ['-updated_at']
        verbose_name = "Car"
        verbose_name_plural = "Cars"

class About(models.Model):
    name = models.CharField(max_length=50)
    intro = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class SocialMedia(models.Model):
    tiktok = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    def __str__(self):
        return "Social Media Links"

class FeaturePost(models.Model):
    post1 = models.URLField(blank=True, null=True)
    post2 = models.URLField(blank=True, null=True)
    post3 = models.URLField(blank=True, null=True)
    def __str__(self):
        return "Feature Posts"

