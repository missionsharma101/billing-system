from django import forms

from apps.billmanagement.models import *


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ("user",)
