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
        fields = ['name', 'description']