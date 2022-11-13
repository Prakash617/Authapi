from django.contrib import admin
from .models import Carousel, Social, Team,Visa

@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ["title",'subTitle','image','slug']
    
@admin.register(Visa)
class VisaAdmin(admin.ModelAdmin):
    list_display = ["name",'image','location','slug']
@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ["link"]
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ["name",'qualification','link','image']