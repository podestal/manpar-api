from django.contrib import admin
from . import models

admin.site.register(models.Category)
admin.site.register(models.Dish)
admin.site.register(models.Table)
admin.site.register(models.OrderItem)
admin.site.register(models.Order)

