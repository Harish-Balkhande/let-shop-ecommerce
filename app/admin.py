from django.contrib import admin
from .models import Customer,Product,Cart,OrderPlaced,orderID

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','locality','city','zipcode','state']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title','selling_price','discounted_price','description','brand','category','product_image']

@admin.register(Cart)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']

@admin.register(OrderPlaced)
class OrderPlacedAdmin(admin.ModelAdmin):
    list_display = ['id','user','customer','product','quantity','ordered_date','status']

@admin.register(orderID)
class AdminOrderID(admin.ModelAdmin):
    list_display = ['id', 'SrNo']