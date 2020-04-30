from django.db import models
from django.urls import reverse

# Create your models here.

class ProjectRegister(models.Model):
    projectTitle=models.CharField(max_length=100)
    projectId=models.IntegerField()
    projectContractNo=models.IntegerField()
    projectSiteLocation=models.CharField(max_length=100)
    projectMailLocation=models.CharField(max_length=100)
    orderNumber=models.IntegerField()
    projectStatus=models.CharField(max_length=100)
    projectRecordedBy=models.CharField(max_length=100)
    txTruckRates=models.IntegerField()
    remarks=models.CharField(max_length=100)

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

