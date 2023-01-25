from django.db import models
from django.contrib.auth.models import AbstractUser,User
from phonenumber_field.modelfields import PhoneNumberField


class Customer(AbstractUser):

    ACTIVE = 'active'
    INACTIVE = 'inactive'

    CHOICE_STATUS = [(ACTIVE, ACTIVE), (INACTIVE, INACTIVE)]

    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField(max_length=100,unique=True)
    phone =PhoneNumberField()
    status = models.CharField(max_length=15, choices=CHOICE_STATUS)
    create_at = models.DateField(auto_now_add=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

