from django.conf import settings
from django.db import models

class Category(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Dish(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    picture = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Table(models.Model):

    number = models.IntegerField(unique=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f'Mesa {self.number}'
    
class Order(models.Model):

    PENDING_DISH = 'P'
    SERVED_DISH = 'S'
    COMPLETED_DISH = 'C'

    ORDER_STATUS_OPTIONS = [
        (PENDING_DISH, 'Pending'),
        (SERVED_DISH, 'Served'),
        (COMPLETED_DISH, 'Completed')
    ]

    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=ORDER_STATUS_OPTIONS, max_length=1)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    

class OrderItem(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    observations = models.TextField(null=True, blank=True)
    quantity = models.PositiveIntegerField()
