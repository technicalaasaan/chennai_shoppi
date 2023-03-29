from rest_framework import routers
from .views import ProdViewsets

shoppy = routers.DefaultRouter()

shoppy.register('product', ProdViewsets)
