from django.contrib import admin
from .models import *

# Register your models here.

class user(admin.ModelAdmin):
    list_display = ['name','email','password','date_joined']
admin.site.register(User,user)

class country(admin.ModelAdmin):
    list_display=['name']
admin.site.register(Country,country)

class state(admin.ModelAdmin):
    list_display=['country','name']
admin.site.register(State,state)

class city(admin.ModelAdmin):
    list_display=['state','name']
admin.site.register(City,city)

class user(admin.ModelAdmin):
    list_display=['user','dob','address','phone','image']
admin.site.register(UserProfile,user)

class cate(admin.ModelAdmin):
    list_display=['cat_name']
admin.site.register(ItemCategory,cate)

class item(admin.ModelAdmin):
    list_display=['user','name','description','category','price','condition','upload_date','image']
    list_filter =['price', 'condition']
    search_fields = ['name']
admin.site.register(Item,item)

class cart(admin.ModelAdmin):
    list_display=['user','item','price','quantity','order_id','order_status']
    list_filter =['price', 'order_status']
    search_fields = ['item']
admin.site.register(ProductCart,cart)

class order(admin.ModelAdmin):
    list_display=['user','item','quantity','total_price','order_date','shipping_address','delivery_date','status']
    list_filter =['status']
    search_fields = ['item']
admin.site.register(Order,order)

class pay(admin.ModelAdmin):
    list_display=['user','order','amount','payment_mode','payment_status','payment_date']
    list_filter =['payment_status']
    search_fields = ['order']
admin.site.register(Payment,pay)

class feedback(admin.ModelAdmin):
    list_display=['user','item','rating','comment','review_date']
    list_filter =['review_date']
    search_fields = ['item']
admin.site.register(Feedback,feedback)

class contact(admin.ModelAdmin):
    list_display=['name','email','subject','message','phone','created_at']
    list_filter =['subject','created_at']
admin.site.register(Contact,contact)