from django.db import models
from product.models import ProductRegister
from django.contrib.auth.models import User


# Create your models here.
class OrderRegister(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    total_price=models.DecimalField(max_digits=10,decimal_places=2)
    discount_rate=models.DecimalField(max_digits=5,decimal_places=4,default=0.0)
    payment_amount=models.DecimalField(max_digits=10,decimal_places=2,default=0.0)
    payment_advance=models.DecimalField(max_digits=10,decimal_places=2,default=0.0)
    timestamp=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=20,default='ORDERED')

    def __str__(self):
        return f'{self.id},{self.total_price}'

class OrderItemsRegister(models.Model):
    order_register=models.ForeignKey(OrderRegister,on_delete=models.CASCADE)
    product=models.ForeignKey(ProductRegister,on_delete=models.CASCADE)
    product_price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.PositiveIntegerField()

    def __str__(self):
        return f'{self.order_register.id},{self.quantity},{self.product_price}'


   

