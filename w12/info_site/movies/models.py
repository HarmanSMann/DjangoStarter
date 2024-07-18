from pyexpat import model
from django.db import models

# Import user model
from django.contrib.auth.models import User
# Import model validators
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

# Create Movie model
class Movie(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    year = models.PositiveIntegerField()
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
    posted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Create review model
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField(max_length=100000)
    rating = models.PositiveIntegerField( models.PositiveIntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)]))

    # If print review, will print user that created revuew
    def __str__(self):
        return f"{self.user.username}: {self.review}"
