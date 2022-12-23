from django.db import models
from django.contrib.auth.models import AbstractUser,User
from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):

    ACTIVE = 'active'
    INACTIVE = 'inactive'

    CHOICE_STATUS = [(ACTIVE, ACTIVE), (INACTIVE, INACTIVE)]

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    phone =PhoneNumberField()
    status = models.CharField(max_length=15, choices=CHOICE_STATUS)
    create_at = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username

