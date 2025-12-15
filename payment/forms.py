from django import forms
from .models import ShippingAddress





class ShippingForm(forms.ModelForm):

    shipping_full_name = forms.CharField(
        label="",   
        max_length=25,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '  Full name   '}),
        required=True
    )
    shipping_email = forms.CharField(
        label="",   
        max_length=300,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '  Email   '}),
        required=True
    )
    shipping_address1 = forms.CharField(
        label="",   
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'آدرس خط 1 را وارد کنید'}),
        required=True
    )
    shipping_address2 = forms.CharField(
        label="",   
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'آدرس خط 2 را وارد کنید'}),
        required=False
    )
    shipping_city = forms.CharField(
        label="",   
        max_length=25,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شهر را وارد کنید'}),
        required=True
    )
    shipping_state = forms.CharField(
        label="",   
        max_length=25,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'استان را وارد کنید'}),
        required=False
    )
    shipping_country = forms.CharField(
        label="",   
        max_length=25,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'کشور را وارد کنید'}),
        required=True
    )
    shipping_zipcode = forms.CharField(
        label="",   
        max_length=25,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'کد پستی را وارد کنید'}),
        required=False
    )




   
    class Meta:
        model = ShippingAddress
        fields = ('shipping_full_name', 'shipping_email', 'shipping_address1', 'shipping_address2', 'shipping_city', 'shipping_state', 'shipping_country', 'shipping_zipcode', )
        
        exclude = ['user',]