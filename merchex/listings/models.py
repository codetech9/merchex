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
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    def __str__(self):
        return f'{self.name}'

class Listing(models.Model):
    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=100)
    sold = models.fields.BooleanField(default=True)
    year = models.fields.IntegerField()
    class Type(models.TextChoices):
        RECORDS = 'RE'
        CLOTHINGS = 'CL'
        POSTERS = 'PO'
        MISCELLANEOUS = 'MI'

    type = models.fields.CharField(choices=Type.choices, max_length=5)
    def __str__(self):
        return f'{self.title}'
