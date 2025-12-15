from django.shortcuts import render, redirect
from .models import Product,Category, Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm, UpdateUserForm, UpdatePasswordForm, UpdateUserInfo
from django.db.models import Q
import json
from cart.cart import Cart

from payment.forms import ShippingForm
from payment.models import ShippingAddress, Order



def user_orders(request):
    if request.user.is_authenticated:
       delivered_orders = Order.objects.filter(user=request.user, status='delivered')
       other_orders = Order.objects.filter(user=request.user).exclude(status='delivered')

       context={
              'delivered': delivered_orders,
                'other': other_orders
       }



       return render(request, 'orders.html', context)

    else:
         messages.success(request, ("برای مشاهده سفارشات ابتدا باید وارد شوید."))      
    
         return redirect('home')

def update_info(request):

    if request.user.is_authenticated: 
       current_user = Profile.objects.get(user__id=request.user.id)
    #    shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
       shipping_user, created = ShippingAddress.objects.get_or_create(user_id=request.user.id)
       
       form = UpdateUserInfo(request.POST or None, instance = current_user)
       shipping_form = ShippingForm(request.POST or None, instance = shipping_user)

       if form.is_valid() or shipping_form.is_valid():
           form.save() 
           shipping_form.save()
           login(request, current_user)
           messages.success(request, ("اطلاعات کاربری  شما با موفقیت ویرایش شد."))
           return redirect('home')          
       return render(request, 'update_info.html', {'form': form, 'shipping_form': shipping_form }) 
    else: 
         messages.success(request, ("برای ویرایش پروفایل ابتدا باید وارد شوید."))      
    
         return redirect('home') 
    

def search(request):

    if request.method == 'POST':

       searched = request.POST['searched']

       searched = Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))
       if not searched:
            messages.success(request, "محصول مورد نظر یافت نشد.")
            return render(request, 'search.html', {})
       else:

            return render(request, 'search.html', {'searched': searched})
    return render(request, 'search.html', {})
    
 


def category_summery(request):
    all_cat = Category.objects.all()
    return render(request, 'category_summery.html',{'category': all_cat})

def helloworld(request):

    all_products = Product.objects.all()
    return render(request, 'index.html',{'products': all_products})

def about(request):
    return render(request, 'about.html')


def login_user(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            current_user = Profile.objects.get(user__id=request.user.id)
            saved_cart = current_user.old_cart
            
            if saved_cart:
                converted_cart = json.loads(saved_cart)
                cart = Cart(request)

                for key, value in converted_cart.items():
                    cart.db_add(product=key, quantity=value)

            messages.success(request, ("شما با موفقیت وارد شدید."))
            return redirect('home')
        else:
            messages.success(request, ("نام کاربری یا رمز عبور اشتباه است."))
            return redirect('login')
    return render(request, 'login.html')

def logout_user(request):
    
    logout(request)
    messages.success(request, ("شما با موفقیت خارج شدید."))

    return redirect('home')
def signup_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("ثبت نام با موفقیت انجام شد."))
            return redirect('home')
        else:
         messages.success(request, ("خطا در ثبت نام. لطفا دوباره تلاش کنید."))
         return redirect('signup')
    else:
       
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})
def update_user(request):
    
    if request.user.is_authenticated:
       current_user = User.objects.get(id=request.user.id)
       user_form = UpdateUserForm(request.POST or None, instance=current_user)
       if user_form.is_valid():
           user_form.save() 
           login(request, current_user)
           messages.success(request, ("پروفایل شما با موفقیت ویرایش شد."))
           return redirect('home')          
       return render(request, 'update_user.html', {'user_form': user_form}) 
    else:
         messages.success(request, ("برای ویرایش پروفایل ابتدا باید وارد شوید."))      
    
         return redirect('home') 

def update_password(request):
  
    if request.user.is_authenticated:
       current_user = User.objects.get(id=request.user.id)
       password_form = UpdatePasswordForm(current_user, request.POST or None)
       if password_form.is_valid():
           password_form.save() 
           login(request, current_user)
           messages.success(request, ("رمز عبور شما با موفقیت ویرایش شد."))
           return redirect('home')          
       return render(request, 'update_password.html', {'password_form': password_form}) 
    else:
         messages.success(request, ("برای ویرایش رمز عبور ابتدا باید وارد شوید."))      
    
         return redirect('home')

    
def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product': product})

def category(request, cat):
    cat=cat.replace("-","")
    try:
       category = Category.objects.get(name=cat)
       
       products = Product.objects.filter(category=category)

       return render(request, 'category.html', {'products': products,"category": category})
       
    except:
        messages.error(request, "دسته بندی مورد نظر یافت نشد.")
        return redirect('home')