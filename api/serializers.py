from rest_framework import serializers
from . import models

class GetDishSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Dish
        fields = ['id', 'name', 'description', 'cost', 'created_at', 'available', 'picture', 'category']

class CreateDishSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Dish
        fields = ['name', 'description', 'cost', 'picture', 'category']

class GetCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = ['id', 'name', 'description']

class CreateCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = ['id', 'name', 'description']

class GetTableSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Table
        fields = ['id', 'number', 'is_available']

class CreateTableSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Table
        fields = ['id', 'number', 'is_available']

class GetOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Order
        fields = ['id', 'table', 'created_at', 'updated_at', 'status']

class CreateOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Order
        fields = ['id', 'table', 'status']

class GetOrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.OrderItem
        fields = ['id', 'dish', 'order', 'quantity']

class CreateOrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.OrderItem
        fields = ['id', 'dish', 'order', 'quantity']