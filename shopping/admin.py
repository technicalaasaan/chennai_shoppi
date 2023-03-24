from django.contrib import admin
from .models import Customer, ProdParent, ProdCategory, Product

# Register your models here.
admin.site.register(Customer)
admin.site.register(ProdParent)
admin.site.register(ProdCategory)
admin.site.register(Product)
