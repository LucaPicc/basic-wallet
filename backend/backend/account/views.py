from django.contrib.auth.models import User

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializer import AccountSerializer, UserOptionSerializer
from .models import Account


class AccountView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            account = Account.objects.get(owner_id=request.GET['userid'])
        except Account.DoesNotExist:
            account = Account.objects.create(owner_id=request.GET['userid'])
        serializer = AccountSerializer(account)

        return Response(serializer.data, status=status.HTTP_200_OK)

class GetUsers(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request, *args, **kwargs):
        users = UserOptionSerializer(User.objects.all().exclude(id=request.GET['userid']), many=True)

        return Response(users.data, status=status.HTTP_200_OK)