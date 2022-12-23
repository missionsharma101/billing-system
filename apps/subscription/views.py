from django.contrib import messages
from django.shortcuts import render, redirect
from apps.subscription.forms import SubscriptionForm
from apps.subscription.models import Subscription
from django.contrib.auth.decorators import login_required


@login_required(login_url='signin')
def subscription_dashboard(request):
    if request.user.groups.filter(permissions__name="Can view group"):
        fil = {}
        if request.method == "POST":
            fil["status"] = request.POST.get("status")
        enquires = Subscription.objects.filter(**fil)
    else:
        print("==========",id)
        # return "hello"
        enquires = Subscription.objects.filter(customer__user__id=request.user.id)

    context = {"enquires": enquires}

    return render(request, "pages/subscription/subdashboard.html", context)

@login_required(login_url='signin')
def subscription_create(request):
    context = dict()
    if request.method == "POST":
        form = SubscriptionForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, "subscription create successfully")
            return redirect("list-subscription")
    else:
        form = SubscriptionForm()
    context["form"] = form
    return render(request, "pages/subscription/add_subscription.html", context)

@login_required(login_url='signin')
def subscription_update(request, pk):
    if request.user.groups.filter(permissions__name="Can add subscription"):
        if request.method == "POST":
            subscription = Subscription.objects.get(id=pk)
            form = SubscriptionForm(request.POST, request.FILES, instance=subscription)
            if form.is_valid():
                form.save()
                messages.success(request, "subscription update successfully")
                return redirect("list-subscription")
        else:
            subscription = Subscription.objects.get(id=pk)
            form = SubscriptionForm(instance=subscription)

        context = {
            "subscription": subscription,
            "form": form,
        }
    else:
        messages.success(request,"you dont have permission to update subscription")    
        return redirect("list-subscription")
    return render(request, "pages/subscription/update.html", context)

@login_required(login_url='signin')
def subscription_delete(request, pk):
    if request.user.groups.filter(permissions__name="Can delete subscription"):
        member = Subscription.objects.get(id=pk)
        member.delete()
        messages.success(request, "Delete successfully")
        return redirect("list-subscription")
    else:  
        messages.success(request,"you dont have permission to delete subscription")
        return redirect("list-subscription")



