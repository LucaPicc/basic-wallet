from rest_framework import serializers
from coins.models import Coin



class AccountSerializer(serializers.Serializer):
    owner=serializers.SerializerMethodField('get_username')
    cvu=serializers.CharField(required=True, max_length=200)
    balance=serializers.SerializerMethodField('get_balance')
    coin = serializers.SerializerMethodField('get_reference_coin')
    funds_blocked = serializers.SerializerMethodField('get_funds_blocked')
    funds_to_be_settled = serializers.SerializerMethodField('get_funds_to_be_settled')


    def get_username(self, obj):
        return obj.owner.username

    def get_balance(self, obj):
        return obj.wallet.get_global_balance()

    def get_reference_coin(self, obj):
        return Coin.objects.get(is_reference=True).short_name

    def get_funds_blocked(self, obj):
        return obj.wallet.get_blocked_balance()

    def get_funds_to_be_settled(self, obj):
        return obj.wallet.get_balance_to_be_settled()