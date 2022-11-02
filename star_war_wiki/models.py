from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Planet(models.Model):
    planet_name = models.CharField()
    description = models.TextField()


    class Meta:
        ordering = ("name")
    
class Movie(models.Model):
    movie_name = models.CharField()
    opening_text = models.TextField()
    director = models.CharField()
    producer = models.CharField()
    budget = models.PositiveIntegerField()
    revenue = models.PositiveIntegerField()
    year = models.PositiveIntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2023)]
    )
    planets = models.ManyToManyField(Planet, related_name="planets", blank=True)
    class Meta:
        ordering = ("year")

class Character(models.Model):
    name = models.CharField()
    movies = models.ManyToManyField(Movie, related_name="movies", blank=True)
    description = models.TextField()
    race = models.CharField()
    profession = models.CharField()

    class Meta:
        ordering = ("name")
