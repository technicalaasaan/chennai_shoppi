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
