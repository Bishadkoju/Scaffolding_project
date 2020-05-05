from django.db import models
from product.models import ProductRegister
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class OrderRegister(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    total_price=models.DecimalField(max_digits=10,decimal_places=2)
    discount_rate=models.DecimalField(max_digits=5,decimal_places=3,default=0)
    discount_amount=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    payment_amount=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    payment_advance=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    timestamp=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=20,default='ORDERED')

    def __str__(self):
        return f'{self.user.username},{self.id},{self.total_price}'

    def get_absolute_url(self):
        return reverse('order_detail',args=[self.id])
    class Meta:
        ordering=['-timestamp',]

class DnCnRegister(models.Model):
    order_register=models.OneToOneField(OrderRegister,on_delete=models.CASCADE)
    timestamp=models.DateTimeField(auto_now_add=True)
    type=models.CharField(max_length=20)
    truck_type=models.CharField(max_length=20)
    truck_rate=models.DecimalField(max_digits=10,decimal_places=2)
    truck_plate_num=models.CharField(max_length=20)
    remarks=models.CharField(max_length=200)
    recorded_by=models.ForeignKey(User,on_delete=models.CASCADE)



class OrderItemsRegister(models.Model):
    order_register=models.ForeignKey(OrderRegister,on_delete=models.CASCADE)
    product=models.ForeignKey(ProductRegister,on_delete=models.CASCADE)
    product_price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.PositiveIntegerField()
    sub_total=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f'{self.order_register.id},{self.quantity},{self.product_price}'



   

