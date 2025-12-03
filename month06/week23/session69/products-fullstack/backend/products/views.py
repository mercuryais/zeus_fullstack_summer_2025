from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category, Product

from .serializers import (
    CategorySerializer,
    ProductSerializer,
    ProductCreateSerializer
)

# ============ Category Views ============
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

# ============ Product Views ============
class ProductListView(generics.ListAPIView):
    """
    GET: Бүх бүтээгдэхүүнүүдийг авах
    Query params:
        - category: ангилалаар шүүх
        - search: нэрээр хайх
        - min_price, max_price: үнээр шүүх
    """
    serializer_class = ProductSerializer
    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True)
        # Ангилалаар шүүх
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category_id=category)
        # Нэрээр хайх
        search = self.request.query_params.get('search')
        if search:
            queryset = queryset.filter(name__icontains=search)
        # Үнээр шүүх
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        return queryset
class ProductCreateView(generics.CreateAPIView):
    """POST: Шинэ бүтээгдэхүүн үүсгэх"""
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Нэг бүтээгдэхүүн авах
    PUT/PATCH: Бүтээгдэхүүн засах
    DELETE: Бүтээгдэхүүн устгах
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
class ProductStatsView(APIView):
    """Бүтээгдэхүүний статистик"""
    def get(self, request):
        total_products = Product.objects.count()
        active_products = Product.objects.filter(is_active=True).count()
        total_categories = Category.objects.count()
        out_of_stock = Product.objects.filter(stock=0).count()
        return Response({
            'total_products': total_products,
            'active_products': active_products,
            'total_categories': total_categories,
            'out_of_stock': out_of_stock
        })