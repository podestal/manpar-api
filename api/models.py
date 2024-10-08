from django.conf import settings
from django.db import models

class Category(models.Model):

    MORNING = 'M'
    EVENING = 'E'
    BOTH = 'B'

    TIME_PERIODS = [
        (MORNING, 'Morning'),
        (EVENING, 'Evening'),
        (BOTH, 'Both'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    time_period = models.CharField(max_length=1, choices=TIME_PERIODS)

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
    
class DishImage(models.Model):

    dish = models.OneToOneField(Dish, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to='dishes/')

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

    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='orders', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=ORDER_STATUS_OPTIONS, max_length=1)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Bill(models.Model):

    table = models.OneToOneField(Table, on_delete=models.CASCADE, related_name='bill')
    

class OrderItem(models.Model):

    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, blank=True)
    bill = models.ForeignKey(Bill, on_delete=models.SET_NULL, null=True, blank=True)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    observations = models.TextField(null=True, blank=True)
    quantity = models.PositiveIntegerField()
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)
