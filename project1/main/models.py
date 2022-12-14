from django.db import models

# Create your models here.

class MyModel1(models.Model):
    image = models.ImageField(upload_to='images', default='')