from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

STATE_CHOICES = (
    ('None', 'Select State'),
    ('Andaman & Nicobar Island', 'Andaman & Nicobar'),
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'ArunachalPradesh'),
    ('Asam', 'Asam'),
    ('Bihar', 'Bihar'),
    ('Chandhighar', 'Chandhighar'),
    ('Chattisghar', 'Chattisghar'),
    ('Dadar & Nagar Haveli', 'Dadar & Nagar Haveli'),
    ('Daman and Diu', 'Daman and Diu'),
    ('Goa', 'Goa'),
    ('Gujarath', 'Gujarath'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himichal Pradesh'),
    ('Keraka', 'Kerala'),
    ('Madhyapradesh', 'Madhyapradesh'),
    ('Maharashtra', 'Maharashtra')
)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 150)
    locality = models.CharField(max_length = 150)
    city = models.CharField(max_length = 150)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES ,max_length = 150)

    def __str__(self):
        return str(self.id) 
    
CATEGORY_CHOICES = (
    ('m', 'Mobile'),
    ('L', 'Laptop'),
    ('TW', 'Top Ware'),
    ('BW', 'Bottom Ware'),    
)
class Product(models.Model):
    title = models.CharField(max_length = 150)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length = 150)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length = 2)
    product_image = models.ImageField(upload_to='product_image', height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return str(self.id)
    
STATUS_CHOICES = (
    ('None', 'Select status'),
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On the way', 'Onthe way'),
    ('Deivered', 'Delivered'),
    ('Cancle', 'Cancle')
)
    
class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length = 150, choices=STATUS_CHOICES, default='Pending')
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

class orderID(models.Model):
    SrNo = models.BigIntegerField()