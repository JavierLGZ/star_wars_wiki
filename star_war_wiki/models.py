from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Planet(models.Model):
    planet_name = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        ordering = ("planet_name",)

    def __str__(self) -> str:
        return self.planet_name
    
class Movie(models.Model):
    movie_name = models.CharField(max_length=200)
    opening_text = models.TextField()
    director = models.CharField(max_length=200)
    producer = models.CharField(max_length=200)
    budget = models.PositiveIntegerField()
    year = models.PositiveIntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2023)]
    )
    planets = models.ManyToManyField(Planet, related_name="planets", blank=True)
    class Meta:
        ordering = ("pk",)
    
    def __str__(self) -> str:
        return f"{self.movie_name} ({self.year})"

class Character(models.Model):
    name = models.CharField(max_length=200)
    movies = models.ManyToManyField(Movie, related_name="movies", blank=True)
    description = models.TextField()

    class Meta:
        ordering = ("name",)
    
    def __str__(self) -> str:
        return self.name
