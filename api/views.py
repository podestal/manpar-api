from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . import serializers
from . import models

class DishViewSet(ModelViewSet):

    queryset = models.Dish.objects.select_related('category')
    allow_http_methods = ['get', 'post', 'patch', 'delete']
    
    def get_serializer_class(self):

        if self.request.method == 'POST':
            return serializers.CreateDishSerializer
        return serializers.GetDishSerializer
    
class CategoryViewSet(ModelViewSet):

    queryset = models.Category.objects.all()
    allow_http_methods = ['get', 'post', 'patch', 'delete']
    
    def get_serializer_class(self):

        if self.request.method == 'POST':
            return serializers.CreateCategorySerializer
        return serializers.GetCategorySerializer
    
class TableViewSet(ModelViewSet):

    queryset = models.Table.objects.all()
    allow_http_methods = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.CreateTableSerializer
        return serializers.GetTableSerializer
    
class OrderViewSet(ModelViewSet):

    queryset = models.Order.objects.select_related('table')
    allow_http_methods = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.CreateOrderSerializer
        return serializers.GetOrderSerializer

class OrderItemViewSet(ModelViewSet):

    queryset = models.OrderItem.objects.select_related('order', 'dish')
    allow_http_methods = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.CreateOrderItemSerializer
        return serializers.GetOrderItemSerializer

