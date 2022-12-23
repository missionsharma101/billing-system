from django.db import models

from apps.billmanagement.models import Customer
class Subscription(models.Model):

    PAID = 'paid'
    UNPAID = 'unpaid'
    CHOICE_SUB_STATUS = [(PAID, PAID), (UNPAID, UNPAID)]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=CHOICE_SUB_STATUS)
    amount = models.FloatField(null=True)
    from_date = models.DateField(auto_now_add=True)
    to_date = models.DateField()

    def __str__(self):
        return self.customer.user.username
