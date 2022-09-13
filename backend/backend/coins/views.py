from .models import Balance, Coin, Transactions
from .serializers import BalanceSerializer, CoinSerializer, TransactionSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class CoinList(ListAPIView):
    permission_classes=[IsAuthenticated]
    queryset=Coin.objects.all()
    serializer_class=CoinSerializer


class TransactionsView(APIView):
    permission_classes = [IsAuthenticated]

    def create_send_transaction(self, transmitter:int, receiver:int, coin:int, amount:float) -> Response:
        balance = Balance.objects.get(owner_id=transmitter, coin_id=coin, category=Balance.REGULAR)
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
                coin_id=coin,
                category=Balance.REGULAR
            )
        except Balance.DoesNotExist:
            balance = Balance.objects.create(
                owner_id=transmitter,
                coin_id=coin,
                balance=0.0000,
                category=Balance.REGULAR
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

    def reception_funds(self, transaction, userid):
        block_found = Balance.objects.get(
            transaction=transaction)

        transaction = Transactions.objects.get(
            id=transaction)

        balance = Balance.objects.get(
            coin=block_found.coin,
            category=Balance.REGULAR,
            owner=transaction.receiver)

        
        balance.balance = balance.balance + block_found.balance
        block_found.delete()
        transaction.valid = True
        
        balance.save()
        transaction.save()

        Transactions.objects.create(
            transmitter_id=userid,
            receiver_id=userid,
            operation=Transactions.RECEPTION,
            coin=transaction.coin,
            amount=transaction.amount
        )

        return Response({'message':'operation acept'}, status=status.HTTP_202_ACCEPTED)

    def withdrawal_funds(self, transmitter:int , coin:int, amount:float):
        try:
            balance = Balance.objects.get(
                owner_id=transmitter,
                coin_id=coin,
                category=Balance.REGULAR
            )

        except Balance.DoesNotExist:
            balance = Balance.objects.create(
                owner_id=transmitter,
                coin_id=coin,
                balance=0.0000,
                category=Balance.REGULAR
            )

        if float(balance.balance) < float(amount):
            return Response({'message': 'insufficient funds'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        
        balance.balance = float(balance.balance) - float(amount)
        balance.save()

        Transactions.objects.create(
            transmitter_id=transmitter,
            receiver_id=transmitter,
            operation=Transactions.WITHDRAWAL,
            coin_id=coin,
            amount=amount
        )

        return Response(BalanceSerializer(balance).data, status=status.HTTP_202_ACCEPTED)

    def get(self, request, *args, **kwargs):
        
        try:
            query = Transactions.objects.get(code=request.GET['code'])
            transaction = TransactionSerializer(query)
            return Response(transaction.data, status=status.HTTP_200_OK)
        
        except KeyError:
            query = Transactions.objects.filter(
                transmitter=request.GET['userid']
            ).order_by('-created')

            transactions = TransactionSerializer(
                query,
                many=True)

            return Response(transactions.data, status=status.HTTP_200_OK)

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

        if operation == Transactions.RECEPTION:
            return self.reception_funds(
                request.data['transaction'],
                request.data['userid']
            )
        
        if operation == Transactions.WITHDRAWAL:
            return self.withdrawal_funds(
                request.data['transmitter'],
                request.data['coin'],
                request.data['amount']
            )

        return Response({'message': 'operation not support'}, status=status.HTTP_406_NOT_ACCEPTABLE)


class BlockedTransactionsView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request, *args, **kwargs):
        query = Balance.objects.filter(
            category=Balance.BLOCKED,
            transaction__receiver=request.GET['userid']
        ).select_related('transaction')

        transactions = [Transactions.objects.get(id=blocked.transaction.id) for blocked in query]

        transaction_serializer = TransactionSerializer(transactions, many=True)

        return Response(transaction_serializer.data, status=status.HTTP_200_OK)
        