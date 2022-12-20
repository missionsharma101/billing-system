from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from apps.billmanagement.forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def get_signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, "Signup successfully")

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
                messages.success(request, "Signin successfully")

                return redirect("/")
    else:
        form = AuthenticationForm()
    return render(request, "pages/signin.html", {"form": form})


def get_logout(request):
    logout(request)
    messages.success(request, "Logout successfully")

    return redirect("signin")

@login_required(login_url='signin')
def dashboard(request):

    fil = {}
    if request.method == "POST":
        fil["status"] = request.POST.get("status")
    enquires = Customer.objects.filter(**fil)
    context = {"enquires": enquires}

    return render(request, "pages/index.html", context)

@login_required(login_url='signin')
def create_customer(request):

    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer Create successfully")
            return redirect("/")
    else:
        form = CustomerForm()
    context = {
        "form": form,
    }
    return render(request, "pages/create_customer.html", context)

@login_required(login_url='signin')
def customer_update(request, pk):
    if request.method == "POST":
        customer = Customer.objects.get(id=pk)
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer update successfully")

            return redirect("dashboard")
    else:
        customer = Customer.objects.get(id=pk)
        form = CustomerForm(instance=customer)

    context = {
        "customer": customer,
        "form": form,
    }
    return render(request, "pages/update_customer.html", context)

@login_required(login_url='signin')
def customer_delete(request, pk):
    customer = Customer.objects.get(id=pk)
    customer.delete()
    messages.success(request, "Delete successfully")
    return redirect("/")
