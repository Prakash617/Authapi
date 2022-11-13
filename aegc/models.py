
from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.\
    
baseUrl = "http://127.0.0.1:8000/"

class Carousel(models.Model):
    title = models.CharField(max_length=200)
    subTitle = models.CharField(max_length=400)
    
    image = models.ImageField(upload_to ='uploads/Carusel',null=True)
    slug = models.CharField(null=True , max_length=1000, blank=True,unique=True)
   
    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def get_imageUrl(self):
        return f'{baseUrl}media/{self.image}'
        
    def get_slug(self):
         if self.slug:
            return 'http://127.0.0.1:8000/api' + self.slug
         else:
            if self.title:
                self.slug = slugify(self.title)
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

class Social(models.Model):
    link = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.link
    
class Team(models.Model):
    name = models.CharField(max_length=75)
    qualification = models.CharField(max_length=100)
    link = models.ForeignKey(Social,on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='uploads/Team',null=True)
    
    def __str__(self):
        return self.name
    
    
    def get_imageUrl(self):
        return f'{baseUrl}media/{self.image}'
    