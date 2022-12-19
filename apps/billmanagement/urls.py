from django.urls import path

from apps.billmanagement.views import *
urlpatterns = [
    path("",dashboard,name="dashboard")
  
]