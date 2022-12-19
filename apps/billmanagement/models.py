from django.db import models
from django.db import models


class Customer(models.Model):

    ACTIVE = 'active'
    INACTIVE = 'inactive'

    CHOICE_STATUS = [(ACTIVE, ACTIVE), (INACTIVE, INACTIVE)]

    name = models.CharField(max_length=100,unique=True)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    status = models.CharField(max_length=15, choices=CHOICE_STATUS)
    create_at = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

