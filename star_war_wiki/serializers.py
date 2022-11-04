from rest_framework import serializers

from .models import Planet, Movie, Character


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'movie_name',
            'opening_text',
            'director',
            'producer',
            'budget',
            'year',
            'planets'
        )

class CharacterSerializer(serializers.ModelSerializer):
    movie_list = MovieSerializer(many=True, read_only=True)
    class Meta:
        model = Character
        fields = (
            'name',
            'description',
            'movie_list',
            'movies'
        )

class PlanetSerializer(serializers.ModelSerializer):
    movie_list = MovieSerializer(many=True, read_only=True)
    class Meta:
        model = Planet
        fields = (
            'planet_name',
            'description',
            'movie_list',
        )
