from django.test import TestCase
import requests

## GET
endpoint = 'http://localhost:8000/api/v1/players/1'

res = requests.get(endpoint)

print(res.json())

# Assert with existing and non existing users

endpoint = 'http://localhost:8000/api/v1/players/-9'

res = requests.get(endpoint)

print(res.json())

endpoint = 'http://localhost:8000/api/v1/players/9999'

res = requests.get(endpoint)

print(res.json())

# Create your tests here.
#class UsersAPITestCase(APITestCase):
#    def setUp(self):
#        
#    def test_list_users(self):
#        url = reverse()
#        response = self.client.get(url)
#        self.assertEqual(response.status_code, 200)
#        self.assertTrue(len(response.data) >= 1)

## GET ALL

endpoint = 'http://localhost:8000/api/v1/players'

res = requests.get(endpoint)

print(res.json())

## POST

endpoint = 'http://localhost:8000/api/v1/players'
request = factory.post('/notes/', {'title': 'new idea'}, content_type='application/json')

res = requests.get(endpoint)

print(res.json())

from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User as DjangoUser
from rest_framework.authtoken.models import Token

class UserCreationTestCase(APITestCase):

    def setUp(self):
        self.user = DjangoUser.objects.create_superuser(username='test',
        password='test')
        self.token = Token.objects.create(user= self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_user_creation(self):
        data = {'username':'Jose', 'age':66}
        res = self.client.post('/api_view/users/', data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_user_creation_menor(self):
        data = {'username':'Jose', 'age':2}
        res = self.client.post('/api_view/users/', data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_creation_no_authorized(self):
        self.client.force_authenticate(user=None)
        data = {'username':'Jose', 'age':66}
        res = self.client.post('/api_view/users/', data)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)