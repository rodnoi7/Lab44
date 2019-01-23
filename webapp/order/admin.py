from django.contrib import admin
from order.models import Employee, Food, Order, OrderFood

# Register your models here.

admin.site.register(Employee)
admin.site.register(Order)
admin.site.register(Food)
admin.site.register(OrderFood)