from django.contrib import admin
from .models import (
    Customer,
    Product,
    Cart,
    OrderPlaced
)


# Register your models here.

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'name', 'locality', 'city', 'zipcode', 'state']


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'selling_price', 'discounted_price', 'description', 'brand', 'category',
                    'product_image']


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'product_id', 'quantity']


@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'customer_id', 'product_id', 'quantity', 'order_date', 'status']

