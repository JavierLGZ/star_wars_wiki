from rest_framework import generics
from django_filters import rest_framework as filters
from .models import Planet, Movie, Character
from .serializers import PlanetSerializer, MovieSerializer, CharacterSerializer

class CharacterFilter(filters.FilterSet):
    class Meta:
        model = Character
        fields = {
            'name': ['contains'],
        }

class CharacterListView(generics.ListAPIView):
    serializer_class = CharacterSerializer
    queryset = Character.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CharacterFilter

class PostCharacterView(generics.ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class RetrieveCharacterView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class PostPlanetView(generics.ListCreateAPIView):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer

class RetrievePlanetView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
    
class PostMovieView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class RetrieveMovieView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer