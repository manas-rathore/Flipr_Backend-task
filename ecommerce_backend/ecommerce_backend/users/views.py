from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView

class SignUpView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class SignInView(TokenObtainPairView):
    pass  # Default implementation works
