from .models import SupplierRegister
from django import forms

class addSupplierForm(forms.ModelForm):
    supplierName=forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Supplier Name'}),
                                  required=True,max_length=100)
    supplierAddress=forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Supplier Address'}),
                                  required=True,max_length=100)
    supplierUrl=forms.URLField(widget=forms.URLInput(
        attrs={'class':'form-control','placeholder':'Supplier URL'}),
                                  required=True,max_length=2083)
    supplierContactPerson=forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Supplier Contact Person'}),
                                  required=True,max_length=100)
    supplierContact1=forms.CharField(widget=forms.NumberInput(
        attrs={'class':'form-control','placeholder':'Supplier Contact 1'}),
                                   required=True,max_length=30)
    supplierContact2=forms.CharField(widget=forms.NumberInput(
        attrs={'class':'form-control','placeholder':'Supplier Contact 2'}),
                                   required=True,max_length=30)
    supplierContactFax=forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Supplier Contact Fax'}),
                                  required=True,max_length=100)
    supplierEmail=forms.EmailField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Supplier Email'}),
                                   required=True,max_length=100)
    class Meta:
        model=SupplierRegister
        fields=[
                'supplierName',
                'supplierAddress',
                'supplierUrl',
                'supplierContactPerson',
                'supplierContact1',
                'supplierContact2',
                'supplierContactFax',
                'supplierEmail'
              ]
