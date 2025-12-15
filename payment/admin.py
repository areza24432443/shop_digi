from django.contrib import admin
from .models import ShippingAddress, Order, orderItem



admin.site.register(ShippingAddress)
# admin.site.register(Order)
admin.site.register(orderItem)

class orderItemInline(admin.TabularInline):

    model = orderItem
    extra =0
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    readonly_fields = ('date_ordered','last_updated')
    inlines = [orderItemInline]


