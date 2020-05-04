from .models import ProductRegister
from django import forms

class addProductForm(forms.ModelForm):
    productName=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Product Name',}),
                                required=True,max_length=100)
    productMaterialItemCode=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Product Material Item Code',}),
                                required=True,max_length=100)
    productBrandNewSellingRate=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Product Brand-New Selling Rate',}),
                                required=True)
    productSecondHandSellingRate=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Product Second Hand Selling Rate',}),
                                required=True)
    productLossRate=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Product Loss Rate',}),
                                required=True)
    productRepairRate=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Product Repair Rate',}),
                                required=True)
    productCleaningRate=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Product Cleaning Rate',}),
                                required=True)
    productDailyRentalRate=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Product Daily Rental Rate',}),
                                required=True)
    productWeeklyRentalRate=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Product Weekly Rental Rate',}),
                                required=True)
    productMonthlyRentalRate=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Product Monthly Rental Rate',}),
                                required=True)
    productDailyHireCharge=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Product Daily Hire Charge',}),
                                required=True)
    productWeeklyHireCharge=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Product Weekly Hire Charge',}),
                                required=True)
    productMonthlyHireCharge=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Product Monthly Hire Charge',}),
                                required=True)
    stock=forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder':'Amount of product in stock ',}),
                                required=True,min_value=0)
    productRecordedBy=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Product Recorded By',}),
                                required=True,max_length=100)
    supplierName=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Supplier Name',}),
                                required=True,max_length=100)
    remarks=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Remarks',}),
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
                'stock',
                'productRecordedBy',
                'supplierName',
                'remarks'
               ]