from django.contrib import admin

from apps.orders.models import Order,UserAddress

admin.site.register(Order)
admin.site.register(UserAddress)