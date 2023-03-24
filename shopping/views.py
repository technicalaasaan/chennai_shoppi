import json

from django.shortcuts import render
from .models import Customer
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import Product
from .form import CustomerForm, CustomerModelForm
from django.views.generic import CreateView, TemplateView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.
def home(request):
    data = Product.objects.all()
    return render(request, 'shopping/home.html', {'name': 'Mohideen', 'data': data})

class Browse(TemplateView):
    template_name = 'shopping/browse.html'

@csrf_exempt
def customer(request): # function based view
    print('request', request.POST)
    if request.method == 'GET':
        filter = Customer.objects.filter(address=request.GET.get('address'))
        obj = filter or Customer.objects.all()
        data = serializers.serialize('json', obj)
        return JsonResponse(json.loads(data), safe=False)
    elif request.method == 'POST':

        # print(form.data.get('user'))
        # when we using forms.Form
        # form = CustomerForm(request.POST)
        # obj = Customer()
        # obj.cus_name = form.data.get('cus_name')
        # obj.address = form.data.get('address')
        # obj.user = User.objects.get(pk=form.data.get('user'))
        # obj.mobile = form.data.get('mobile')
        # obj.state = form.data.get('state')
        # obj.dob = form.data.get('dob')
        # obj.save()
        # end

        # print(json.loads(form.data))
        # data = json.loads(request.body)
        # print('data', data)
        # data['user'] = User.objects.get(pk=data['user'])
        # res = Customer.objects.create(**data)
        # print(res, res.__dict__)
        return JsonResponse([], safe=False)
    return JsonResponse({k:v for k,v in res.__dict__.items() if k != '_state'}, safe=False)

def customer_view(request):
    data = {}
    form = CustomerModelForm(request.POST)
    if form.is_valid():
        form.save()
    data['form'] = form
    return render(request, 'customer.html', data)

class CustomerView(CreateView):
    form_class = CustomerModelForm
    template_name = 'customer.html'
    success_url = '/customer'


class CustomerDetailView(DetailView):
    model = Customer
    template_name =  'customer_detail.html' # 'templates/shopping/customer_detail.html'

class CustomerListView(ListView):
    model = Customer
    template_name =  'customer_detail.html' # 'templates/shopping/customer_list.html'

class CustomerUpdateView(UpdateView):
    model = Customer
    fields = "__all__"
    template_name = 'customer.html' # 'templates/shopping/customer_form.html'
    success_url = '/customer'

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer_delete.html'
    success_url = '/customer'


