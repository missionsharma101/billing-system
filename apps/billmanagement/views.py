from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from apps.billmanagement.forms import *


def get_signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("/")
    else:
        form = UserCreationForm()
    return render(request, "pages/signup.html", {"form": form})


def get_signin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
    else:
        form = AuthenticationForm()
    return render(request, "pages/signin.html", {"form": form})


def get_logout(request):
    logout(request)
    return redirect("signin")


def dashboard(request):

    fil = {}
    if request.method == "POST":
        fil["status"] = request.POST.get("status")
    enquires= Customer.objects.filter(**fil)
    print(enquires)
    context={
        "enquires":enquires
    }    

    return render(request, "pages/index.html", context)


def create_customer(request):
    context = dict()
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("/")
    else:
        form = CustomerForm()
    context["form"] = form
    return render(request, "pages/create_customer.html", context)


def customer_update(request, pk):
    if request.method == "POST":
        customer = Customer.objects.get(id=pk)
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()

            return redirect("dashboard")
    else:
        customer = Customer.objects.get(id=pk)
        form = CustomerForm(instance=customer)

    context = {
        "customer": customer,
        "form": form,
    }
    return render(request, "pages/update_customer.html", context)


def customer_delete(pk):
    try:
        member = Customer.objects.get(id=pk)
        member.delete()
        return redirect("/")
    except Customer.DoesNotExist:
        return redirect("/")



