from django.db import models

# Create your models here.

class social_accounts(models.Model):
    platform = models.CharField(max_length=100)
    urls = models.URLField(max_length=200)
    icons = models.CharField(max_length=100)


class cars_details(models.Model):
    car_name = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    car_image = models.ImageField(upload_to='car_photos')

class contacts(models.Model):
     name = models.CharField(max_length=100)
     email = models.EmailField()
     subject = models.CharField(max_length=200)
     message = models.TextField()

def __str__(self):
        return self.car_name
