from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from account.models import Company
# Create your models here.

class ProjectRegister(models.Model):
    STATUS_TYPES=(('Running','Running'),('Completed','Completed'))
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    projectTitle=models.CharField(max_length=100)
    projectId=models.IntegerField()
    projectContractNo=models.IntegerField()
    projectSiteLocation=models.CharField(max_length=100)
    projectMailLocation=models.EmailField(blank=True)
    orderNumber=models.IntegerField(default=0)
    projectStatus=models.CharField(max_length=100,choices=STATUS_TYPES)
    projectRecordedBy=models.ForeignKey(User,on_delete=models.CASCADE)
    txTruckRates=models.IntegerField()
    amount_paid =models.DecimalField(max_digits=10,decimal_places=2,default=0)
    amount_to_be_paid =models.DecimalField(max_digits=10,decimal_places=2,default=0)
    remarks=models.CharField(max_length=255)

    def __str__(self):
        return self.projectTitle
    def get_absolute_url(self):
        return reverse('project_detail',args=[self.id])
    def get_update_url(self):
        return reverse('project_update',args=[self.id])
    def get_delete_url(self):
        return reverse('project_delete',args=[self.id])
    class Meta:
        ordering=['-projectTitle',]

