from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category, Product

from .serializers import (
    CategorySerializer,
    ProductSerializer,
    ProductCreateSerializer
)

class CategoryListCreateView(generics.ListCreateAPIView):
    """
    GET: Бүх ангилалуудыг авах
    POST: Шинэ ангилал үүсгэх
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Нэг ангилал авах
    PUT/PATCH: Ангилал засах
    DELETE: Ангилал устгах
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class ProductListView(generics.ListAPIView):

    serializer_class = ProductSerializer
    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True)
        category = self.request.query_params.get('category')
        search = self.request.query_params.get('search')  

        if category:
            queryset = queryset.filter(category_id=category)
        if search:
            queryset = queryset.filter(name__icontains=search)

        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        return queryset

class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
