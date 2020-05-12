from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from account.models import Company,Profile


class CreateUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Username'}),
               required=True,max_length=50)
    first_name=forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'First Name'}),
               required=True,max_length=50)
    last_name=forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Last Name'}),
               required=True,max_length=50)
    email=forms.CharField(widget=forms.EmailInput(
        attrs={'class':'form-control','placeholder':'Email Address'}),
               required=True,max_length=50)
    password1=forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control','placeholder':'Password'}),
               required=True,max_length=50)
    password2=forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control','placeholder':'Confirm Password'}),
               required=True,max_length=50)
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2']

    def clean_email(self):
        email=self.cleaned_data['email']
        try:
            match=User.objects.get(email=email)
        except:
            return self.cleaned_data['email']
        raise forms.ValidationError("Email already exists")


class CreateProfileForm(forms.ModelForm):
    user=forms.ModelChoiceField(queryset=User.objects.all(),required=False,widget=forms.HiddenInput())
    company=forms.ModelChoiceField(queryset=Company.objects.all(),empty_label="Select Company")
    recorded_by=forms.ModelChoiceField(queryset=User.objects.all(),required=False,widget=forms.HiddenInput())

    class Meta:
        model=Profile
        fields='__all__'
        #exclude=['user']

class UpdateUserForm(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Username'}),
               required=True,max_length=50)
    first_name=forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'First Name'}),
               required=True,max_length=50)
    last_name=forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Last Name'}),
               required=True,max_length=50)
    class Meta:
        model=User
        fields=['first_name','last_name','username']

class UpdateProfileForm(forms.ModelForm):

    def clean_username(self):
        username=self.cleaned_data['username']
        try:
            match=User.objects.get(username=username)
        except:
            return self.cleaned_data['username']
        raise forms.ValidationError('Username Already Exists ')

    class Meta:
        model=Profile
        fields=['contact_number','profile_picture']





