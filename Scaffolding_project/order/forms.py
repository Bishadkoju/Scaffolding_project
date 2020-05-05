from django import forms
from .models import *

class ApproveQuotationForm(forms.ModelForm):

    class Meta:
        model=OrderRegister
        fields=['discount_rate',
                'payment_advance']

class PaymentConfirmForm(forms.ModelForm):
    
    class Meta:
        model=OrderRegister
        fields=['payment_amount',]

class DnCnForm(forms.ModelForm):
    type=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Type of DN CN',}),
                                required=True)
    truck_rate=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Truck Rate',}),
                                required=True)
    truck_type=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Type of Truck',}),
                                required=True)
    truck_plate_num=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Truck plate Number',}),
                                required=True)
    remarks=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Remarks',}),
                                required=True)


    class Meta:
        model=DnCnRegister
        exclude=['order_register','recorded_by']
        #fields='__all__'

