
from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.\
    
baseUrl = "http://127.0.0.1:8000/"

class Carousel(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to ='uploads/Carusel',null=True)
    slug = models.CharField(null=True , max_length=1000, blank=True,unique=True)
   
    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    def get_imageUrl(self):
        return f'{baseUrl}media/{self.image}'
        
    def get_slug(self):
         if self.slug:
            return 'http://127.0.0.1:8000/api' + self.slug
         else:
            if self.name:
                self.slug = slugify(self.name)
                self.save()

                return 'http://127.0.0.1:8000/api' + self.slug
            else:
                return ''
            
class Visa(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to ='uploads/Visa',null=True)
    location = models.CharField(max_length = 100)
    slug = models.CharField(null=True , max_length=1000, blank=True,unique=True)
    
    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_imageUrl(self):
        return f'{baseUrl}media/{self.image}'