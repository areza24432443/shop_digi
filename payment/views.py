from django.shortcuts import render, redirect, get_object_or_404
from cart.cart import Cart
from .forms import ShippingForm
from .models import ShippingAddress, Order, orderItem
from django.contrib.auth.models import User
from django.contrib import messages
from shop.models import Product



def payment_success(request):
    return render(request,'payment/payment_success.html',{})


def checkout(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    total = cart.get_total() 

    if request.user.is_authenticated:

        # shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
        shipping_user, created = ShippingAddress.objects.get_or_create(user_id=request.user.id)
        shipping_form = ShippingForm(request.POST or None, instance= shipping_user)
        return render(request,'payment/checkout.html',{'cart_products': cart_products, 'quantities': quantities ,'total': total,'shipping_form': shipping_form})
    else:
       
       shipping_form = ShippingForm(request.POST or None)


       return render(request,'payment/checkout.html',{'cart_products': cart_products, 'quantities': quantities ,'total': total,'shipping_form': ShippingForm})
    

def confirm_order(request):
    if request.method == 'POST':
       cart = Cart(request)
       cart_products = cart.get_prods()
       quantities = cart.get_quants()
       total = cart.get_total() 

       user_shipping = request.POST
       request.session['user_shipping'] = user_shipping

       
       return render(request,'payment/confirm_order.html',{'cart_products': cart_products, 'quantities': quantities ,'total': total,'shipping_info': user_shipping})

               
        

    else:
        messages.success(request, ("لطفا ابتدا فرم را پر کنید. "))
        return redirect('checkout')

    # return render(request,'payment/confirm_order.html',{})

def process_order(request):
    # Here you would integrate with a payment gateway
    # For this example, we'll assume payment is always successful

    # Clear the cart after successful payment
    if request.method == 'POST':
        cart = Cart(request)
        cary_products = cart.get_prods()
        quantities = cart.get_quants()
        total = cart.get_total()
        user_shipping = request.session.get('user_shipping')
        full_name = user_shipping['shipping_full_name'] 
        email = user_shipping['shipping_email']
        full_address = f"{user_shipping['shipping_address1']}\n {user_shipping['shipping_address2']}\n {user_shipping['shipping_city']}\n {user_shipping['shipping_state']}\n {user_shipping['shipping_zipcode']}\n {user_shipping['shipping_country']}"
        if request.user.is_authenticated:
            user = request.user
            new_order = Order(
                user=user,
                full_name=full_name,
                email=email,
                ShippingAddress=full_address,
                amount_paid=total
            )
            new_order.save()
            
          
            odr = get_object_or_404(Order, id=new_order.pk)
            for product in cary_products:
               prod = get_object_or_404(Product, id=product.id)
               if product.is_sale:
                  price = product.sale_price
               else:
                  price = product.price

                  for k,v in quantities.items():
                      if int(k) == product.id:
                            new_order = orderItem(
                                order=odr,
                                product=prod,
                                user=user,
                                price=price,
                                quantity=v
                            )
                            new_order.save()

            for key in list(request.session.keys()):
                 if key == 'session_key':
                      del request.session[key]
                          

        messages.success(request, ("سفارش با موفقیت ثبت شد. "))
        return redirect('home')  
    
    else:
        
        new_order = Order(
                
                full_name=full_name,
                email=email,
                ShippingAddress=full_address,
                amount_paid=total
            )
        new_order.save()



        odr = get_object_or_404(Order, id=new_order.pk)
        for product in cary_products: 
               prod = get_object_or_404(Product, id=product.id)
               if product.is_sale:
                  price = product.sale_price
               else:
                  price = product.price

                  for k,v in quantities.items():
                      if int(k) == product.id:
                            new_order = orderItem(
                                order=odr,
                                product=prod,
                                
                                price=price,
                                quantity=v 
                            )
                            new_order.save()
        for key in list(request.session.keys()):
                 if key == 'session_key':
                      del request.session[key]

        messages.success(request, ("خطا در پردازش سفارش. "))
        return redirect('home')

    