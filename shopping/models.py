from django.contrib.auth.models import User
from django.db import models

states = (
    ('Assam', 'Assam'),
    ('Karnataka', 'Karnataka'),
    ('Bihar', 'Bihar'),
    ('Maharashtra', 'Maharashtra'),
    ('Meghalaya', 'Meghalaya'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('West Bengal', 'West Bengal'),
    ('Gujarat', 'Gujarat'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Odisha', 'Odisha'),
    ('Rajasthan', 'Rajasthan'),
    ('Nagaland', 'Nagaland'),
    ('Telangana', 'Telangana'),
    ('Sikkim', 'Sikkim'),
    ('Haryana', 'Haryana'),
    ('Manipur', 'Manipur'),
    ('Kerala', 'Kerala'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Punjab', 'Punjab'),
    ('Mizoram', 'Mizoram'),
    ('Goa', 'Goa'),
    ('Jharkhand', 'Jharkhand'),
    ('Uttarakhand', 'Uttarakhand'),
    ('Tripura', 'Tripura'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Other', 'Other')
)

# Create your models here.
class Customer(models.Model):
    cus_id = models.AutoField(primary_key=True)
    cus_name = models.CharField(max_length=100, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    mobile = models.CharField(max_length=10, null=False)
    state = models.CharField(max_length=100, choices=states, null=False, default='Other')
    dob = models.DateField()

    def __str__(self):
        return self.cus_name

    class Meta:
        db_table = 'customer'

class ProdParent(models.Model):
    prod_parent_id = models.AutoField(primary_key=True)
    parent_name = models.CharField(max_length=100)

    def __str__(self):
        return self.parent_name

    def __repr__(self):
        return self.__str__()

class ProdCategory(models.Model):
    cat_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    parent = models.ForeignKey(ProdParent, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.parent.parent_name} - {self.category_name}"

    def __repr__(self):
        return self.__str__()

class Product(models.Model):
    prod_id = models.AutoField(primary_key=True)
    prod_name = models.CharField(max_length=200, null=False)
    prod_category = models.ForeignKey(ProdCategory, on_delete=models.CASCADE)
    prod_images = models.ImageField(upload_to='products/')
    prod_actual_price = models.FloatField()
    prod_discount = models.FloatField(default=0.0)
    prod_description = models.TextField(null=True)
    prod_colour = models.CharField(max_length=50, null=True)
    prod_qty = models.IntegerField(default=0)

    def __str__(self):
        return self.prod_name

    def __repr__(self):
        return self.__str__()
