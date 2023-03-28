"""chennai_shoppi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from shopping.views import home, login, logout, Browse, customer, customer_view, CustomerView, CustomerDeleteView, CustomerDetailView, CustomerListView, CustomerUpdateView

urlpatterns = [
    path('', home),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('browse/', Browse.as_view(), name='browse'),
    path('customer', customer),
    path('customer/<pk>/', CustomerDetailView.as_view()),
    path('customer/<pk>/update', CustomerUpdateView.as_view()),
    path('customer/<pk>/delete', CustomerDeleteView.as_view()),
    path('customer/', CustomerListView.as_view()),
    path('customer_entry/', customer_view),
    path('customer_add/', CustomerView.as_view()),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
