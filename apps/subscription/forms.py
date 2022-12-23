from django import forms
from apps.subscription.models import *


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        exclude = ("customer",)
