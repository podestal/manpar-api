from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from . import serializers
from . import models

class DishViewSet(ModelViewSet):

    queryset = models.Dish.objects.select_related('category')
    http_method_names = ['get', 'post', 'patch', 'delete']
    
    def get_serializer_class(self):

        if self.request.method == 'POST':
            return serializers.CreateDishSerializer
        if self.request.method == 'PATCH':
            return serializers.UpdateDishSerializer
        return serializers.GetDishSerializer
    
class DishImageViewSet(ModelViewSet):

    queryset = models.DishImage.objects.select_related('dish')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['dish']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.CreateDishImageSerializer
        return serializers.GetDishImageSerializer
    
class CategoryViewSet(ModelViewSet):

    queryset = models.Category.objects.all()
    http_method_names = ['get', 'post', 'patch', 'delete']
    
    def get_serializer_class(self):

        if self.request.method == 'POST':
            return serializers.CreateCategorySerializer
        return serializers.GetCategorySerializer
    
class TableViewSet(ModelViewSet):

    queryset = models.Table.objects.prefetch_related('orders')
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.CreateTableSerializer    
        return serializers.GetTableSerializer
    
class OrderViewSet(ModelViewSet):

    queryset = models.Order.objects.select_related('table', 'created_by')
    http_method_names = ['get', 'post', 'patch', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['table', 'status']


    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.CreateOrderSerializer
        return serializers.GetOrderSerializer
    
    def get_serializer_context(self):
        return {'user_id': self.request.user}

class OrderItemViewSet(ModelViewSet):

    queryset = models.OrderItem.objects.select_related('order', 'dish')
    http_method_names = ['get', 'post', 'patch', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['order']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.CreateOrderItemSerializer
        return serializers.GetOrderItemSerializer

