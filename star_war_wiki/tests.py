from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


from .models import Planet, Movie, Character

class Test_Create_Post(APITestCase):
    fixtures = ["fixture.json"]

    def test_get_movie(self):
        url = reverse('star_wars:createcharacter')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
