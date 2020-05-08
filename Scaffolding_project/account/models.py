from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    TYPE_CHOICE=(('self','Self'),('client','Client'))
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    province =models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street=models.CharField(max_length=50)
    type =models.CharField(max_length=10,default='client',choices=TYPE_CHOICE)
    price =models.DecimalField(max_digits=10,decimal_places=2)
    contact_number=models.CharField(max_length = 15)
    website=models.URLField(blank=True)
    
    def __str__(self):
        return self.name



    
