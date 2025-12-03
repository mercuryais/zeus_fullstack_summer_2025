from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    """Category-г JSON болгох serializer"""
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at']
class ProductSerializer(serializers.ModelSerializer):
    """Product-г JSON болгох serializer"""
    category_name = serializers.CharField(source='category.name', read_only=True)
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'price',
            'stock',
            'category',
            'category_name',
            'image',
            'is_active',
            'created_at',
            'updated_at'
        ]
class ProductCreateSerializer(serializers.ModelSerializer):
    """Product үүсгэх serializer"""
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'stock',
            'category',
            'image',
            'is_active'
        ]