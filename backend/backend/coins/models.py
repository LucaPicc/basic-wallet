from datetime import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
import hashlib
from django.db.models import F



class Coin(models.Model):
    FIAT = 'fiat'
    CRIPTO = 'cripto'
    DEFAULT_VALUE_VS_REFERENCE = 1.0000

    COIN_CATEGORIES = [
        (FIAT, 'fiat'),
        (CRIPTO, 'cripto')
    ]

    name = models.CharField(max_length=250, blank=False, null=False)
    short_name = models.CharField(max_length=5, blank=False, null=False)
    category = models.CharField(choices=COIN_CATEGORIES, max_length=100, default=FIAT, blank=False, null=False)
    is_reference = models.BooleanField(default=False)
    value_vs_reference = models.DecimalField(max_digits=10, decimal_places=4, default=DEFAULT_VALUE_VS_REFERENCE)

    def __str__(self) -> str:
        return f'{self.name}({self.value_vs_reference})'


class Transactions(models.Model):
    SEND = 'send'
    RECEPTION = 'reception'
    DEPOSIT = 'deposit'
    WITHDRAWAL = 'withdrawal'

    TRANSACTIONS_TYPE = [
        (SEND, 'send'),
        (RECEPTION, 'reception'),
        (DEPOSIT, DEPOSIT),
        (WITHDRAWAL, WITHDRAWAL)
    ]

    transmitter = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False, db_index=True, related_name='transimitter')
    receiver = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False, db_index=True, related_name='receiver')
    operation = models.CharField(choices=TRANSACTIONS_TYPE, default=SEND,max_length=10, blank=False, null=False, db_index=True)
    code = models.CharField(max_length=255, db_index=True, default='', blank=True, null=False)
    coin = models.ForeignKey(Coin, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=10, decimal_places=4)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    valid = models.BooleanField(default=False)

    def _generate_code(self, transmitter: str, receiver:str, operation:str, created:str) -> str:
        code = f'{transmitter}{receiver}{operation}{created}'
        return hashlib.md5(code.encode('utf-8')).hexdigest()
    
    def save(self, *args, **kwargs) -> None:
        self.created = timezone.now()
        self.code = self._generate_code(
            self.transmitter.username,
            self.receiver.username,
            self.operation,
            str(self.created)
        )
        return super(Transactions, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        def get_symbol(operation:str) -> str:
            if operation == self.SEND:
                return '->'
            if operation == self.RECEPTION:
                return '<-'
            if operation == self.DEPOSIT:
                return '++'
            if operation == self.WITHDRAWAL:
                return '--'
        
        return f'[{self.id}]{self.transmitter} {get_symbol(self.operation)} {self.receiver} ({self.coin.name}{self.amount})'


class Balance(models.Model):
    REGULAR = 'regular'
    BLOCKED = 'blocked'

    BALANCE_TYPE = [
        (REGULAR, 'regular'),
        (BLOCKED, 'blocked')
    ]

    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    coin = models.ForeignKey(Coin, on_delete=models.PROTECT)
    category = models.CharField(choices=BALANCE_TYPE, default=REGULAR, max_length=20)
    balance = models.DecimalField(max_digits=10, decimal_places=4)
    transaction = models.ForeignKey(Transactions, on_delete=models.PROTECT, default=None, null=True, blank=True)


class Wallet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    balances = models.ManyToManyField(Balance)

    def get_global_balance(self):
        balances = self.balances.filter(category=Balance.REGULAR) \
            .annotate(value_reference = F('coin__value_vs_reference')) \
            .values('value_reference', 'balance')

        total = 0
        for balance in balances:
            total = total + balance['value_reference'] * balance['balance']

        return total

    def get_blocked_balance(self):
        balances = Balance.objects.filter(
            transaction__transmitter=self.owner,
            category=Balance.BLOCKED) \
            .annotate(value_reference = F('coin__value_vs_reference')) \
            .values('value_reference', 'balance')
        
        total = 0
        for balance in balances:
            total = total + balance['value_reference'] * balance['balance']

        return total

    def get_balance_to_be_settled(self):
        balances = Balance.objects.filter(
            transaction__receiver=self.owner,
            category=Balance.BLOCKED) \
            .annotate(value_reference = F('coin__value_vs_reference')) \
            .values('value_reference', 'balance')
        
        total = 0
        for balance in balances:
            total = total + balance['value_reference'] * balance['balance']
        
        return total

