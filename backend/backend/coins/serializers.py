from rest_framework import serializers

class CoinSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    name = serializers.CharField(required=True, max_length=100)
    short_name = serializers.CharField(required=True, max_length=10)
    category = serializers.CharField(required=True, max_length=100)
    is_reference = serializers.BooleanField(required=True)
    value_vs_reference = serializers.FloatField(required=True)

class BalanceSerializer(serializers.Serializer):
    coin = serializers.CharField(required=True, max_length=100)
    category = serializers.CharField(required=True, max_length=100)
    balance = serializers.FloatField(required=True)

class TransactionSerializer(serializers.Serializer):
    coin = serializers.SerializerMethodField('get_coin_name')
    operation = serializers.CharField(required=True, max_length=100)
    amount = serializers.FloatField(required=True)
    code=serializers.CharField(required=True, max_length=100)

    def get_coin_name(self, obj):
        return obj.coin.name