from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from star_war_wiki import views

app_name='star_wars'

urlpatterns = [
    path('', views.CharacterListView.as_view(), name='listcharacters'),
    path('characters/<int:pk>/', views.RetrieveCharacterView.as_view(), name= 'updatecharacter'),
    path('characters/', views.PostCharacterView.as_view(), name='createcharacter'),
    path('planets/', views.PostPlanetView.as_view(), name='createplanet'),
    path('planets/<int:pk>/', views.RetrievePlanetView.as_view(), name='updateplanet'),
    path('movies/', views.PostMovieView.as_view(), name='createmovie'),
    path('movies/<int:pk>/', views.RetrieveMovieView.as_view(), name='updatemovie'),
]

urlpatterns = format_suffix_patterns(urlpatterns)