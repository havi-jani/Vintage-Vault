from django.db import models
from django.core.validators import MinValueValidator , MaxValueValidator , MaxLengthValidator, MinLengthValidator
from django.utils.safestring import mark_safe
# Create your models here.


status = [('pending', 'Pending'), ('shipped', 'Shipped'),('delivered', 'Delivered')]
method = [('credit_card', 'Credit Card'), ('debit_card', 'Debit Card'),('paypal', 'PayPal'), ('other', 'Other')]
order = [('pending', 'Pending'),('ordered', 'Ordered')]
pay_status = [('pending', 'Pending'), ('completed', 'Completed'),('failed', 'Failed')]

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField()
    date_joined = models.DateField()

    def __str__(self):
        return f"{self.name}"
    
class Country(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name}"

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"
    
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dob = models.DateField()
    address = models.TextField()
    phone = models.CharField(validators=(MinLengthValidator(10), MaxLengthValidator(10)))
    img = models.ImageField(upload_to='user_image/', blank=True)

    def __str__(self):
        return f"{self.user.name}"
    
    def image(self):
        if self.img:
            return mark_safe(f'<img src="{self.img.url}" width="500" height="500" style="object-fit: contain;" />')
        return '(No img)'

    img.short_description = 'Image Preview'

class ItemCategory(models.Model):
    cat_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.cat_name}"

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    price = models.CharField()
    condition = models.CharField(max_length=100)
    upload_date = models.DateField(auto_now=True)
    img = models.ImageField(upload_to='item_image/')

    def __str__(self):
        return f"{self.name }"
    
    def image(self):
        if self.img:
            return mark_safe(f'<img src="{self.img.url}" width="500" height="500" style="object-fit: contain;" />')
        return '(No img)'

    img.short_description = 'Image Preview'

class ProductCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    price = models.CharField()
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    order_id = models.IntegerField(auto_created=True)
    order_status = models.CharField(choices=order , default='pending')

    def __str__(self):
        return f"{self.item.name}"
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    total_price = models.CharField(max_length=100)
    order_date = models.DateField(auto_now=True)
    shipping_address = models.TextField()
    delivery_date = models.DateField()
    status = models.CharField(max_length=50, choices=status, default='pending')

    def __str__(self):
        return f"{self.item.name}"

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.CharField()
    payment_mode = models.CharField(choices=method)
    payment_status = models.CharField(choices=pay_status , default='pending')
    payment_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.user.name}"
    
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    rating = models.FloatField(validators=[MaxValueValidator(5)])
    comment = models.CharField(max_length=100)
    review_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.item.name }{self.user.name}"
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    phone = models.CharField(validators=(MinLengthValidator(10), MaxLengthValidator(10)))
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.name}"