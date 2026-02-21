from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Block, Stall, MenuItem, TimeSlot, Order, OrderItem

admin.site.register(Block)
admin.site.register(Stall)
admin.site.register(MenuItem)
admin.site.register(TimeSlot)
admin.site.register(Order)
admin.site.register(OrderItem)