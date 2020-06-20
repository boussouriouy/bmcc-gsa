from django.db import models

# Create your models here
class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    is_present = models.BooleanField(default=True)
    flyer = models.ImageField(upload_to='images')
    description = models.TextField(blank=False)
    
    def __str__(self):
        return self.title
    
class Document(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='images')
    
    def __str__(self):
        return self.title 


