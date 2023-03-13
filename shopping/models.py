from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Customer(models.Model):
    cus_id = models.AutoField(primary_key=True)
    cus_name = models.CharField(max_length=100, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    mobile = models.CharField(max_length=10, null=False)
    dob = models.DateField()

    def __str__(self):
        return self.cus_name

    class Meta:
        db_table = 'customer'
