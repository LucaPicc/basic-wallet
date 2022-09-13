from django.contrib import admin
from .models import Coin, Wallet, Balance, Transactions

@admin.register(Coin)
class CoinModelAdmin(admin.ModelAdmin):
    fields = ['name', 'category', 'value_vs_reference', 'is_reference']
    list_display = ['name', 'category', 'value_vs_reference']

@admin.register(Wallet)
class WalletModelAdmin(admin.ModelAdmin):
    list_display = ['get_owner_name', 'get_global_balance']

    def get_owner_name(self, obj:Wallet) -> str:
        return obj.owner.username

    def get_global_balance(self, obj:Wallet) -> float:
        return obj.get_global_balance()

    get_owner_name.short_description = 'owner name'
    get_global_balance.short_description = 'wallet balance'

@admin.register(Balance)
class BalanceModelAdmin(admin.ModelAdmin):
    fields = ['owner', 'coin', 'category', 'balance', 'transaction']
    list_display = ['get_owner_name', 'get_coin_name', 'category', 'balance', 'transaction']

    def get_owner_name(self, obj:Balance) -> str:
        return obj.owner.username

    def get_coin_name(self, obj:Balance) -> str:
        return obj.coin.name

    get_owner_name.short_description = 'owner name'
    get_coin_name.short_description = 'coin name'

@admin.register(Transactions)
class TransactionsModelAdmin(admin.ModelAdmin):
    list_display=['transmitter', 'receiver', 'operation', 'get_coin_name', 'code', 'amount', 'created']

    def get_coin_name(self, obj:Balance) -> str:
        return obj.coin.name
    
    get_coin_name.short_description = 'coin name'