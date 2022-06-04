from django.db import models
from  django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Band(models.Model):
    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(max_length=50)
    biography = models.fields.CharField(max_length=100)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900),    MaxValueValidator(2022)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
    """
    genre = models.fields.CharField(choices=Genre.choises, max_length=5)
    """

class Listing(models.Model):
    title = models.fields.CharField(max_length=100)
