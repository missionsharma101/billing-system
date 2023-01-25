from django.urls import path

from apps.billmanagement.views import *

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("signup", get_signup, name="signup"),
    path("signin", get_signin, name="signin"),
    path("logout", get_logout, name="logout"),
    path("update-customer/<int:pk>",customer_update,name="update-customer"),
    path("delete-customer/<int:pk>",customer_delete,name="delete-customer"),
]
