from django.urls import path

from apps.subscription.views import *
urlpatterns = [

    path("list-subscription",subscription_dashboard,name="list-subscription"),
    path("create-subscription",subscription_create,name="create-subscription"),
    path("update-subscription/<int:pk>",subscription_update,name="update-subscription"),
    path("delete-subscription/<int:pk>/",subscription_delete,name="delete-subscription"),
    path("send-mail",sendmail,name="send-mail")


]