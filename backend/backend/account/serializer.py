from rest_framework import serializers



class AccountSerializer(serializers.Serializer):
    owner=serializers.SerializerMethodField('get_username')
    cvu=serializers.CharField(required=True, max_length=200)
    balance=serializers.SerializerMethodField('get_balance')


    def get_username(self, obj):
        return obj.owner.username

    def get_balance(self, obj):
        return obj.wallet.get_global_balance()