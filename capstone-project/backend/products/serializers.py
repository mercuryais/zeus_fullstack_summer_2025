from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at']

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'detailed_description',
            'price',
            'sale',
            'stock',
            'category',
            'category_name',
            'sku',
            'image',
            'is_active',
            'created_at',
            'updated_at'
        ]

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'detailed_description',
            'price',
            'stock',
            'category',
            'sale',
            'sku',
            'image',
            'is_active'
        ]