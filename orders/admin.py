from django.contrib import admin

from .models import Order, OrderItem

class OrderProductInLineAdmin(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [OrderProductInLineAdmin]

admin.site.register(Order, OrderAdmin)
