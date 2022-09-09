from account.models import Account
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status


class Login(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data['username']
        password = request.data['password']
        # print('username', username)
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'message': 'user does not exist'}, status=status.HTTP_403_FORBIDDEN)
        
        if not check_password(password, user.password):
            return Response({'message': 'invalid password'}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            token = Token.objects.get(user=user)
            token.delete()
            token = Token.objects.create(user=user)
        except Token.DoesNotExist:
            token = Token.objects.create(user=user)

        return Response({'userid': str(user.id), 'token':token.key}, status=status.HTTP_200_OK)


class CreateAccount(APIView):
    def post(self, request):
        try:
            first_name = request.data['first-name']
            last_name = request.data['last-name']
            username = f'{first_name}.{last_name}'
            
            new_user = User.objects.create(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=request.data['email'],
                password=request.data['password']
            )

            Account.objects.create(owner=new_user)

            token = Token.objects.create(user=new_user)

            return Response(
                {
                    'user-id': new_user.id,
                    'token': token.key
                },
                status=status.HTTP_201_CREATED
            )
        except:
            return Response(
                {
                    'message': 'invalid'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
