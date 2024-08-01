from rest_framework import serializers
from . import models

class GetDishSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Dish
        fields = ['id', 'name', 'description', 'cost', 'created_at', 'available', 'picture', 'category', 'image']

class CreateDishSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Dish
        fields = ['id', 'name', 'description', 'cost', 'available', 'picture', 'category']

class UpdateDishSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Dish
        fields = ['id', 'name', 'description', 'cost', 'available', 'picture', 'category']

class GetDishImageSerializer(serializers.ModelSerializer):

    class Meta: 
        model = models.DishImage
        fields = ['id', 'image']

class CreateDishImageSerializer(serializers.ModelSerializer):

    class Meta: 
        model = models.DishImage
        fields = ['id', 'image', 'dish']

class GetCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = ['id', 'name', 'description']

class CreateCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = ['id', 'name', 'description']

class GetOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Order
        fields = ['id', 'table', 'created_at', 'updated_at', 'status', 'created_by']

class CreateOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Order
        fields = ['id', 'table', 'status']

    def create(self, validated_data):
        user = self.context['user_id']
        return models.Order.objects.create(created_by=user, **validated_data)

class GetTableSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Table
        fields = ['id', 'number', 'is_available', 'orders']

    

class CreateTableSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Table
        fields = ['id', 'number', 'is_available']


class GetOrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.OrderItem
        fields = ['id', 'dish', 'order', 'quantity', 'observations']

class CreateOrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.OrderItem
        fields = ['id', 'dish', 'order', 'quantity', 'observations']