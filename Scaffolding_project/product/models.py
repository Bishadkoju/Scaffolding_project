from django.db import models
from django.urls import reverse

# Create your models here.
class ProductRegister(models.Model):
    productName= models.CharField(max_length=100)
    productMaterialItemCode= models.CharField(max_length=100)
    productBrandNewSellingRate= models.DecimalField(max_digits=10, decimal_places=2)
    productSecondHandSellingRate= models.DecimalField(max_digits=10, decimal_places=2)
    productLossRate=models.DecimalField(max_digits=10, decimal_places=2)
    productRepairRate=models.DecimalField(max_digits=10, decimal_places=2)
    productCleaningRate=models.DecimalField(max_digits=10, decimal_places=2)
    productDailyRentalRate=models.DecimalField(max_digits=10, decimal_places=2)
    productWeeklyRentalRate=models.DecimalField(max_digits=10, decimal_places=2)
    productMonthlyRentalRate=models.DecimalField(max_digits=10, decimal_places=2)
    productDailyHireCharge=models.DecimalField(max_digits=10, decimal_places=2)
    productWeeklyHireCharge=models.DecimalField(max_digits=10, decimal_places=2)
    productMonthlyHireCharge=models.DecimalField(max_digits=10, decimal_places=2)
    stock=models.PositiveIntegerField()
    productRecordedBy=models.CharField(max_length=100)
    supplierName=models.TextField(blank=True)
    remarks=models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self):
        return reverse('product_detail',args=[self.id])

    def get_update_url(self):
        return reverse('product_update',args=[self.id])

    def get_delete_url(self):
        return reverse('product_delete',args=[self.id])

    def __str__(self):
        return self.productName

    class Meta:
        ordering=['productName']