from unicodedata import category
from coins.models import Balance
from coins.serializers import BalanceSerializer, TransactionSerializer
from coins.models import Coin, Transactions
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework.test import APITestCase
from rest_framework.test import APIClient


class CoinApiTest(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(
            username='admin',
            email='a@admin.com',
            password=make_password('a123456')
        )

        self.user2 = User.objects.create(
            username='test',
            email='test@test.com',
            password=make_password('test')
        )

        self.token = Token.objects.create(user=self.user)
        # self.client.credentials(Authorization='Token ' + self.token.key)
        self.client.force_authenticate(user=self.user)
        self.coin = Coin.objects.all().first()

    def test_create_deposit(self, **kwargs):
        url = reverse('transactions')

        data = {
            'operation': Transactions.DEPOSIT,
            'transmitter': self.user.id,
            'coin': self.coin.id,
            'amount': 100
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        
        transaction = TransactionSerializer(
            Transactions.objects.get(
                transmitter=self.user,
                operation=Transactions.DEPOSIT
            )
        )

        balance = BalanceSerializer(
            Balance.objects.get(
                owner=self.user,
                coin=self.coin,
                category=Balance.REGULAR
            )
        )
        self.assertEqual(
            response.data,
            {
                'transaction': transaction.data,
                'balance': balance.data
            }
        )

    def test_create_withdrawal(self, **kwargs):
        url = reverse('transactions')

        data = {
            'operation': Transactions.WITHDRAWAL,
            'transmitter': self.user.id,
            'coin': self.coin.id,
            'amount': 100
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_406_NOT_ACCEPTABLE)
        
        balance = Balance.objects.get(
            owner=self.user,
            category=Balance.REGULAR,
            coin=self.coin
        )

        balance.balance = 200.00000
        balance.save()

        response = self.client.post(url, data)

        balance = Balance.objects.get(
            owner=self.user,
            category=Balance.REGULAR,
            coin=self.coin
        )

        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(response.data, BalanceSerializer(balance).data)

