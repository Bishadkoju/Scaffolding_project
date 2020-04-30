from .models import ProductRegister
from django import forms

class addProductForm(forms.ModelForm):
    productName=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Product Name','class':'form-control ',}),
                                required=True,max_length=100)
    productMaterialItemCode=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Product Material Item Code','class':'form-control',}),
                                required=True,max_length=100)
    productBrandNewSellingRate=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Product Brand-New Selling Rate','class':'form-control',}),
                                required=True)
    productSecondHandSellingRate=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Product Second Hand Selling Rate','class':'form-control',}),
                                required=True)
    productLossRate=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Product Loss Rate','class':'form-control',}),
                                required=True)
    productRepairRate=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Product Repair Rate','class':'form-control',}),
                                required=True)
    productCleaningRate=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Product Cleaning Rate','class':'form-control',}),
                                required=True)
    productDailyRentalRate=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Product Daily Rental Rate','class':'form-control',}),
                                required=True)
    productWeeklyRentalRate=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Product Weekly Rental Rate','class':'form-control',}),
                                required=True)
    productMonthlyRentalRate=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Product Monthly Rental Rate','class':'form-control',}),
                                required=True)
    productDailyHireCharge=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Product Daily Hire Charge','class':'form-control',}),
                                required=True)
    productWeeklyHireCharge=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Product Weekly Hire Charge','class':'form-control',}),
                                required=True)
    productMonthlyHireCharge=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Product Monthly Hire Charge','class':'form-control',}),
                                required=True)
    productRecordedBy=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Product Recorded By','class':'form-control',}),
                                required=True,max_length=100)
    supplierName=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Supplier Name','class':'form-control',}),
                                required=True,max_length=100)
    remarks=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Remarks','class':'form-control',}),
                                required=True,max_length=200)
    
    
    class Meta:
        model=ProductRegister
        fields=[
                'productName',
                'productMaterialItemCode',
                'productBrandNewSellingRate',
                'productSecondHandSellingRate',
                'productLossRate',
                'productRepairRate',
                'productCleaningRate',
                'productDailyRentalRate',
                'productWeeklyRentalRate',
                'productMonthlyRentalRate',
                'productDailyHireCharge',
                'productWeeklyHireCharge',
                'productMonthlyHireCharge',
                'productRecordedBy',
                'supplierName',
                'remarks'
               ]