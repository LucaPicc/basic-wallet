import hashlib

from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

from coins.models import Wallet, Balance, Coin

class Account(models.Model):
    owner = models.OneToOneField(User, on_delete=models.PROTECT)
    cvu = models.CharField(max_length=255, blank=False, null=False)
    wallet = models.OneToOneField(Wallet, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)

    def _generate_cvu(self):
        cvu = f'{self.owner.username}{str(self.created)}'
        return hashlib.md5(cvu.encode('utf-8')).hexdigest()
    
    def _create_wallet(self):
        coins = Coin.objects.all()
        balances = [Balance(
            owner=self.owner,
            coin=coin,
            balance=0
        ) for coin in coins]

        Balance.objects.bulk_create(balances)
        del balances

        owner_balances = Balance.objects.filter(owner=self.owner)

        wallet = Wallet.objects.create(
            owner=self.owner,
        )

        wallet.balances.set(owner_balances)

        return wallet


    def save(self, *args, **kwargs) -> None:
        self.created = timezone.now()
        self.cvu = self._generate_cvu()
        self.wallet = self._create_wallet()
        super(Account, self).save(*args, **kwargs)
