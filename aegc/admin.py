from django.contrib import admin
from .models import Carousel,Visa

@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ["name",'image','slug']
    
@admin.register(Visa)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ["name",'image','location','slug']