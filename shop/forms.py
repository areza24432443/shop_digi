
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,SetPasswordForm
from django import forms
from .models import Profile




class UpdateUserInfo(forms.ModelForm):
  
    phone = forms.CharField(
        label="",   
        max_length=25,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شماره تلفن خود را وارد کنید'}),
        required=False
    )
    address1 = forms.CharField(
        label="",   
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'آدرس خط 1 را وارد کنید'}),
        required=False
    )
    address2 = forms.CharField(
        label="",   
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'آدرس خط 2 را وارد کنید'}),
        required=False
    )
    city = forms.CharField(
        label="",   
        max_length=25,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شهر را وارد کنید'}),
        required=False
    )
    state = forms.CharField(
        label="",   
        max_length=25,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'استان را وارد کنید'}),
        required=False
    )
    country = forms.CharField(
        label="",   
        max_length=25,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'کشور را وارد کنید'}),
        required=False
    )
    zipcode = forms.CharField(
        label="",   
        max_length=25,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'کد پستی را وارد کنید'}),
        required=False
    )

    class Meta:
        model = Profile
        fields = ('phone', 'address1', 'address2', 'city', 'state', 'country', 'zipcode', )

class UpdatePasswordForm(SetPasswordForm):

     
    new_password1 = forms.CharField(
        label="",   
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder': 'رمز عبور جدید را وارد کنید',
            'name': 'new_password1',
            'type': 'password'

            })
    )

    new_password2 = forms.CharField(
        label="",   
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder': 'دوباره رمز جدید را وارد کنید',
            'name': 'new_password2',
            'type': 'password'

            })
    )

class SignUpForm(UserCreationForm):

    first_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خود را وارد کنید'})
    )
    last_name = forms.CharField(
        label="",   
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی خود را وارد کنید'})
    )

        
    email = forms.EmailField(
        label="",   
        max_length=100,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل خود را وارد کنید'})
         
         )
    username = forms.CharField(
        label="",   
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی خود را وارد کنید'})
    )
    password1 = forms.CharField(
        label="",   
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder': 'رمز عبور بالای 8 کاراکتر را وارد کنید',
            'name': 'password',
            'type': 'password'

            })
    )

    password2 = forms.CharField(
        label="",   
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder': 'دوباره رمز را وارد کنید',
            'name': 'password',
            'type': 'password'

            })
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name','email','username', 'password1', 'password2', )

class UpdateUserForm(UserChangeForm):

    password = None
    first_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خود را وارد کنید'}),
        required=False
    )
    last_name = forms.CharField(
        label="",   
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی خود را وارد کنید'}),
        required=False
    )

        
    email = forms.EmailField(
        label="",   
        max_length=100,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل خود را وارد کنید'}),
         required=False
         )
    username = forms.CharField(
        label="",   
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی خود را وارد کنید'}),
        required=False
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name','email','username', )