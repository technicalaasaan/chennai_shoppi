import json

from django.shortcuts import render
from .models import Customer
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, 'home.html')

@csrf_exempt
def customer(request): # function based view
    if request.method == 'GET':
        print(request.GET)
        data = serializers.serialize('json', Customer.objects.filter(address=request.GET.get('address')))
        return JsonResponse(json.loads(data), safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        data['user'] = User.objects.get(pk=data['user'])
        res = Customer.objects.create(**data)
        # print(res, res.__dict__)
    return JsonResponse({k:v for k,v in res.__dict__.items() if k != '_state'}, safe=False)