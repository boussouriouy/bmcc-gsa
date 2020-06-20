from django.db import models
from datetime import date
# Create your models here.
class Member(models.Model):
    image = models.ImageField(upload_to='images')
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=15)
    major = models.CharField(max_length=200)
    eboard = models.CharField(max_length=5)
    position = models.CharField(max_length=100)
    alumni = models.CharField(max_length=5)
    term = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    