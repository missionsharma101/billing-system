from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.billmanagement.models import *


class CustomerForm(UserCreationForm):
    class Meta:
        model = Customer
        fields=["username","email","phone"]

class CustomerUpdate(forms.ModelForm):
    class Meta:
        model = Customer
        fields=["username","email","phone"]

