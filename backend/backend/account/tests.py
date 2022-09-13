from account.models import Account
from account.serializer import AccountSerializer
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework.test import APITestCase
from rest_framework.test import APIClient


class AccountTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(
            username='admin',
            email='a@admin.com',
            password=make_password('a123456')
        )

        self.token = Token.objects.create(user=self.user)
        # self.client.credentials(Authorization='Token ' + self.token.key)
        self.client.force_authenticate(user=self.user)

    def test_create_account(self, **kwargs):
        url = reverse('create_account')

        data = {
            'first-name': 'test',
            'last-name': 'test',
            'email': 'test@test.com',
            'password': 'test'
        }


        response = self.client.post(url, data)

        correct_response = {
            'userid': User.objects.get(username='test.test').id,
            'token': Token.objects.get(user__username='test.test').key
        }

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, correct_response)

    def test_get_account(self, **kwargs):
        url = reverse('account')

        data = {
            'userid': self.user.id
        }
        response = self.client.get(url, data)

        account = AccountSerializer(Account.objects.get(owner=self.user)).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, account)
    
    def test_get_users(self, **kwargs):
        url = reverse('users')

        response = self.client.get(url, {'userid': self.user.id})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_login(self, **kwargs):
        url = reverse('auth')
        
        data = {
            'username': 'admin',
            'password': 'a123456'
        }

        response = self.client.post(url, data)

        correct_response = {
            'userid': str(self.user.id),
            'token': Token.objects.get(user=self.user).key
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, correct_response)
        self.assertNotEqual(response.data['token'], self.token)

        data = {
            'username': 'admin',
            'password': 'error'
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, {'message': 'invalid password'})
