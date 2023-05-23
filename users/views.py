from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken, Token
from rest_framework.response import Response
from .serializer import UserSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status

# Create your views here.

# This deals with the user login and generates a token and sends in the response
class ObtainToken(ObtainAuthToken):
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UserSerializer(user)
        user_data = user_serializer.data
        return Response({
            'token' : token.key,
            'user' : user_data
        })

# This  registers the user in our data base and returns a message based on circumstances
class RegisterUser(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        data['password'] = make_password(data['password']) # hash password
        user = User.objects.create(**data)
        
        if user:
            return Response({"message" : "Created Account Successfully"},status=status.HTTP_201_CREATED )
        else:
            return Response({"messsage" : "Bad Request, Account Was Not created"}, status=HTTP_404_BAD_REQUEST)
    