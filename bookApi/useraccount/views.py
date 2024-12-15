from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from .models import ApplicationUser
from django.contrib.auth import authenticate
from post_api.middleware import APIKeyAuthentication

class SignupView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if not username or not password:
            return Response({'error': 'username, email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        user = ApplicationUser.objects.create(
            username=username,
            email=email,
            password=make_password(password)
        )
        return Response({'message': 'User created successfully', 'api_key': user.api_key}, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            return Response({'message': 'Login successful', 'api_key': user.api_key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

class ProfileView(APIView):
    
    authentication_classes = [APIKeyAuthentication]
    
    def post(self, request):
        user = request.user
        return Response({'username': user.username, 'email': user.email}, status=status.HTTP_200_OK)
                        