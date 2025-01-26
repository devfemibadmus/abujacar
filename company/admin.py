from django import forms
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.models import Group
from .models import Image, Car, About, SocialMedia, FeaturePost


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'name', 'email', 'address', 'intro')
    search_fields = ('name', 'email', 'address')
    fields = ('name', 'intro', 'email', 'address')

    def has_add_permission(self, request):
        return self.model.objects.count() == 0
    
    def model_name(self, obj):
        return "Edit about"

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'tiktok_link', 'facebook_link', 'instagram_link', 'youtube_link', 'twitter_link')
    search_fields = ('tiktok', 'facebook', 'instagram', 'youtube', 'twitter')
    fields = ('tiktok', 'facebook', 'instagram', 'youtube', 'twitter')

    def has_add_permission(self, request):
        return self.model.objects.count() == 0

    def model_name(self, obj):
        return "Edit links"

    def extract_username(self, url):
        if not url:
            return ""
        if url.endswith('/'):
            url = url[:-1]
        return url.split('/')[-1] if url else ""

    def tiktok_link(self, obj):
        username = self.extract_username(obj.tiktok)
        return format_html('<a href="{}" target="_blank">{}</a>', obj.tiktok, username)

    def facebook_link(self, obj):
        username = self.extract_username(obj.facebook)
        return format_html('<a href="{}" target="_blank">{}</a>', obj.facebook, username)

    def instagram_link(self, obj):
        username = self.extract_username(obj.instagram)
        return format_html('<a href="{}" target="_blank">{}</a>', obj.instagram, username)

    def youtube_link(self, obj):
        username = self.extract_username(obj.youtube)
        return format_html('<a href="{}" target="_blank">{}</a>', obj.youtube, username)

    def twitter_link(self, obj):
        username = self.extract_username(obj.twitter)
        return format_html('<a href="{}" target="_blank">{}</a>', obj.twitter, username)

@admin.register(FeaturePost)
class FeaturePostAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'post1_link', 'post2_link', 'post3_link')
    search_fields = ('post1', 'post2', 'post3')
    fields = ('post1', 'post2', 'post3')

    def has_add_permission(self, request):
        return self.model.objects.count() == 0

    def model_name(self, obj):
        return "Edit link"

    def post1_link(self, obj):
        return format_html(f'<a href="{obj.post1}" target="_blank">{obj.post1}</a>') if obj.post1 else ""

    def post2_link(self, obj):
        return format_html(f'<a href="{obj.post2}" target="_blank">{obj.post2}</a>') if obj.post2 else ""

    def post3_link(self, obj):
        return format_html(f'<a href="{obj.post3}" target="_blank">{obj.post3}</a>') if obj.post3 else ""

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

class ImageInline(admin.TabularInline):
    model = Image
    extra = 0
    min_num = 2
    max_num = 15
    can_delete = True
    
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'type', 'variant', 'brand', 'condition', 'color')
    list_filter = ('type', 'condition', 'year')
    search_fields = ('make__name', 'year')
    inlines = [ImageInline]
    form = CarForm
    

admin.site.unregister(Group)


