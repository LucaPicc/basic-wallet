from .models import Balance, Coin, Transactions
from .serializers import BalanceSerializer, CoinSerializer, TransactionSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class CoinList(APIView):
    permission_classes=[IsAuthenticated]
    
    def get(self, request):
        serializer = CoinSerializer(Coin.objects.all(), many=True)
        return Response(serializer.data)


class TransactionsView(APIView):
    permission_classes = [IsAuthenticated]

    def create_send_transaction(self, transmitter:int, receiver:int, coin:int, amount:float) -> Response:
        balance = Balance.objects.get(owner_id=transmitter, coin_id=coin)
        if not float(balance.balance) >= float(amount):
            return Response({'message': 'insufficient funds'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        transaction = Transactions.objects.create(
            transmitter_id=transmitter,
            receiver_id=receiver,
            coin_id=coin,
            amount=amount,
            operation=Transactions.SEND
        )

        block_found = Balance.objects.create(
            owner_id=transmitter,
            coin_id=coin,
            category=Balance.BLOCKED,
            balance=amount,
            transaction=transaction
        )

        balance.balance = float(balance.balance) - float(amount)

        balance.save()

        block_serializer = BalanceSerializer(block_found)
        transaction_serializer = TransactionSerializer(transaction)

        return Response(
            {
                'block_found': block_serializer.data,
                'transaction': transaction_serializer.data
            },
            status=status.HTTP_202_ACCEPTED
        )
    
    def create_deposit_transaction(self, transmitter:int, coin:int, amount:float) -> Response:
        transaction = Transactions.objects.create(
            transmitter_id=transmitter,
            receiver_id=transmitter,
            operation=Transactions.DEPOSIT,
            coin_id=coin,
            amount=amount,
            valid=True
        )
        try:
            balance = Balance.objects.get(
                owner_id=transmitter,
                coin_id=coin
            )
        except Balance.DoesNotExist:
            balance = Balance.objects.create(
                owner_id=transmitter,
                coin_id=coin,
                balance=0.0000
            )
        balance.balance = float(balance.balance) + float(amount)
        balance.save()

        transaction_serializer = TransactionSerializer(transaction)
        balance_serializer = BalanceSerializer(balance)

        return Response(
            {
                'transaction': transaction_serializer.data,
                'balance': balance_serializer.data
            },
            status=status.HTTP_202_ACCEPTED
        )

    def get(self, request):
        
        transactions = [{
            'code': transactions[0],
            'name': transactions[1]
        } for transactions in Transactions.TRANSACTIONS_TYPE]

        return Response(transactions, status=status.HTTP_200_OK)

    def post(self, request):
        operation = request.data['operation']
        if operation == Transactions.DEPOSIT:
            return self.create_deposit_transaction(
                request.data['transmitter'],
                request.data['coin'],
                request.data['amount']
            )
        
        if operation == Transactions.SEND:
            return self.create_send_transaction(
                request.data['transmitter'],
                request.data['receiver'],
                request.data['coin'],
                request.data['amount']
            )
        


        return Response({'message': 'operation not support'}, status=status.HTTP_406_NOT_ACCEPTABLE)
