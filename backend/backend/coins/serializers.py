from rest_framework import serializers

class CoinSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    name = serializers.CharField(required=True, max_length=100)
    short_name = serializers.CharField(required=True, max_length=10)
    category = serializers.CharField(required=True, max_length=100)
    is_reference = serializers.BooleanField(required=True)
    value_vs_reference = serializers.FloatField(required=True)

class BalanceSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    coin = serializers.CharField(required=True, max_length=100)
    category = serializers.CharField(required=True, max_length=100)
    balance = serializers.FloatField(required=True)

class TransactionSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    coin = serializers.SerializerMethodField('get_coin_name')
    operation = serializers.CharField(required=True, max_length=100)
    amount = serializers.FloatField(required=True)
    code=serializers.CharField(required=True, max_length=100)
    created=serializers.DateTimeField(required=True, format='%Y-%m-%d %H:%m:%S')
    receiver=serializers.SerializerMethodField('get_receiver_name')
    transmitter=serializers.SerializerMethodField('get_transmitter_name')

    def get_coin_name(self, obj):
        return obj.coin.short_name

    def get_receiver_name(self, obj):
        return obj.receiver.username

    def get_transmitter_name(self, obj):
        return obj.transmitter.username