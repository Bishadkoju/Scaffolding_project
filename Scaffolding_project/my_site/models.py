from django.db import models

# Create your models here.
class ProductRegister(models.Model):
    name= models.CharField(max_length=100)
    itemCode= models.CharField(max_length=100)
    sellingRate= models.DecimalField(max_digits=10, decimal_places=2)
    cleaningRate=models.DecimalField(max_digits=10, decimal_places=2)
    dailyRentalRate=models.DecimalField(max_digits=10, decimal_places=2)
    stock=models.PositiveIntegerField()
    
    
  
    class Meta:
        ordering=['name']

