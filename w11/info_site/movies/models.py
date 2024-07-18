from pyexpat import model
from django.db import models
# Create your models here.
# Create Movie model
class Movie(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    # Attribute to store when movie was created, update only once when created
    # created = model.DateTimeField(auto_now_add=True)
    # Override string representation of object
    
    def __str__(self):
        # Return movie name when printing movie model
        return self.name
