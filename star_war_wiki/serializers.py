from rest_framework import serializers

from .models import Planet, Movie, Character


class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = (
            'planet_name',
            'description',
        )

class MovieSerializer(serializers.ModelSerializer):
    planet_list = PlanetSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = (
            'movie_name',
            'opening_text',
            'director',
            'producer',
            'budget',
            'revenue',
            'year',
            'planet_list'
        )

class CharacterSerializar(serializers.ModelSerializer):
    movie_list = MovieSerializer(many=True, read_only=True)
    class Meta:
        model = Character
        fields = (
            'name',
            'description',
            'race',
            'profession',
            'movie_list',
        )