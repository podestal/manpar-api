from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . import serializers
from . import models

class DishViewSet(ModelViewSet):

    queryset = models.Dish.objects.select_related('category')
    
    def get_serializer_class(self):

        if self.request.method == 'POST':
            return serializers.CreateDishSerializer
        return serializers.GetDishSerializer
    
class CategoryViewSet(ModelViewSet):

    queryset = models.Category.objects.all()
    
    def get_serializer_class(self):

        if self.request.method == 'POST':
            return serializers.CreateCategorySerializer
        return serializers.GetCategorySerializer

