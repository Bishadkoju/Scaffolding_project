from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Company(models.Model):
    TYPE_CHOICE=(('self','Self'),('client','Client'))
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    province =models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street=models.CharField(max_length=50)
    type =models.CharField(max_length=10,default='client',choices=TYPE_CHOICE)
    amount_paid =models.DecimalField(max_digits=10,decimal_places=2,default=0)
    amount_to_be_paid =models.DecimalField(max_digits=10,decimal_places=2,default=0)
    contact_number=models.CharField(max_length = 15)
    website=models.URLField(blank=True)
    remarks=models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    company=models.ForeignKey(Company,on_delete=models.CASCADE,null=True)
    contact_number=models.CharField(max_length=15)
    recorded_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='+',null=True)
    profile_picture=models.ImageField(default='profile_pics/avatar.png',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()
        img=Image.open(self.profile_picture.path)

        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.profile_picture.path)



    


    
