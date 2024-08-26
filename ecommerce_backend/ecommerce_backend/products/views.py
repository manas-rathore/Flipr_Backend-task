from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
