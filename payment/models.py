from django.db import models
from django.contrib.auth.models import User
from shop.models import Product,Profile,Category
from django.db.models.signals import post_save
from django_jalali.db import models as jmodels
from django.utils.timezone import now
import jdatetime



class ShippingAddress(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    shipping_full_name = models.CharField(max_length=250)
    shipping_email = models.CharField(max_length=300)
    shipping_phone = models.CharField(max_length=25, blank=True)
    shipping_address1 = models.CharField(max_length=250, blank=True)
    shipping_address2 = models.CharField(max_length=250, blank=True, null=True)
    shipping_city = models.CharField(max_length=25, blank=True)
    shipping_state = models.CharField(max_length=25, blank=True, null=True)
    shipping_country = models.CharField(max_length=25, blank=True)
    shipping_zipcode = models.CharField(max_length=25,  default='iran',null=True)
    shipping_old_cart = models.CharField(max_length=200,blank=True,null=True)


    class Meta:
         verbose_name_plural = 'Shipping Address'

    def __str__(self):
     
         return f'Shipping Address - {str(self.shipping_full_name)}'
    
    def create_profile(sender,instance,created, **kwargs):
            if created:
                user_profile = Profile(user=instance)
                user_profile.save()
    def create_shipping_user(sender,instance,created, **kwargs):
            if created:
                shipping_user = ShippingAddress(user=instance)
                shipping_user.save()

class Order(models.Model):
    STATUS_ORDERS = (
        ('Pending', 'درانتظازپرداخت'),
        ('Processing', 'درحال پردازش'),
        ('Shipped', 'ارسال شده به پست'),
        ('delivered', 'تحویل شد'),
    )
    
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    full_name = models.CharField(max_length=250)
    email = models.CharField(max_length=300)
    ShippingAddress = models.TextField(max_length=5000)
    amount_paid = models.DecimalField(max_digits=12, decimal_places=0)
    date_ordered = jmodels.jDateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_ORDERS, default='Pending')
    last_updated = jmodels.jDateTimeField(auto_now=True)



    def save(self, *args, **kwargs):
        if self.pk:
           old_status = Order.objects.get(pk=self.pk).status

           if old_status != self.status:
               self.last_updated = jdatetime.datetime.now()

        super().save(*args, **kwargs)

    def __str__(self):
        return f'Order - {str(self.id)}'
     
      
class orderItem(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    quantity = models.PositiveBigIntegerField(default=1)
    price = models.DecimalField(max_digits=12, decimal_places=0)
    

    def __str__(self):
        if self.user is not None:
           
           return f'Order Item - {str(self.id)}- for {self.user}'
        else:
           return f'Order Item - {str(self.id)}'