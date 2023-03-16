from django import forms
from .models import states
from django.contrib.auth.models import User
from .models import Customer

class CustomerForm(forms.Form):
    cus_name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=200)
    mobile = forms.CharField(max_length=10)
    user = forms.ModelChoiceField(queryset=User.objects.all())
    state = forms.ChoiceField(choices=states)
    dob = forms.DateField()

class CustomerModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

        widgets = {
            'cus_name': forms.TextInput(attrs={'class': 'form-control'})
        }
