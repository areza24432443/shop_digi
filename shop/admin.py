from django.contrib import admin
from . import models
from django.contrib.auth.models import User


admin.site.register(models.Category)
admin.site.register(models.Customer)
admin.site.register(models.Product)
admin.site.register(models.Order)
admin.site.register(models.Profile)


class ProfileInline(admin.StackedInline):
    model = models.Profile
    
class UserAdmin(admin.ModelAdmin):
    model = models.User
    inlines = [ProfileInline,]
    fields = ['username', 'first_name', 'last_name', 'email']

admin.site.unregister(models.User)
admin.site.register(User, UserAdmin)


