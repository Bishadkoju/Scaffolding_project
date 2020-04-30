from django import forms
from .models import ProjectRegister

class addProjectForm(forms.ModelForm):
    projectTitle=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Project Title'}),
                                 required=True,max_length=100)
    projectId=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Project ID'}),
                                 required=True)
    projectContractNo=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Project Contract No'}),
                                 required=True)
    projectSiteLocation=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Project Site Location'}),
                                 required=True,max_length=100)
    projectMailLocation=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Project Mail Location'}),
                                 required=True,max_length=100)
    orderNumber=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Order Number'}),
                                 required=True)
    projectStatus=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Project Status'}),
                                 required=True,max_length=100)
    projectRecordedBy=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Project Recorded By'}),
                                 required=True,max_length=100)
    txTruckRates=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Tx Truck Rates'}),
                                 required=True)
    remarks=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Remarks'}),
                                 required=True,max_length=200)
    class Meta:
        model=ProjectRegister
        fields=[
                'projectTitle',
                'projectId',
                'projectContractNo',
                'projectSiteLocation',
                'projectMailLocation',
                'orderNumber',
                'projectStatus',
                'projectRecordedBy',
                'txTruckRates',
                'remarks'
               ]