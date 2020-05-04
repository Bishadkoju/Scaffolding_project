from django.contrib import admin
from .models import OrderItemsRegister,OrderRegister
# Register your models here.
admin.site.register(OrderRegister)
admin.site.register(OrderItemsRegister)
