from django.shortcuts import render,redirect
from apps.subscription.forms import SubscriptionForm
from apps.subscription.models import Subscription

def subscription_dashboard(request):
    context={}
    context["enquires"]=Subscription.objects.all()
    return render(request,"pages/subscription/subdashboard.html",context)



def subscription_create(request):
    context = dict()
    if request.method == "POST":
        form = SubscriptionForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("/")
    else:
        form = SubscriptionForm()
    context["form"] = form
    return render(request, "pages/subscription/subdashboard.html", context)


def subscription_update(request, pk):
    if request.method == "POST":
        subscription = Subscription.objects.get(id=pk)
        form = SubscriptionForm(request.POST, request.FILES, instance=subscription)
        if form.is_valid():
            form.save()

            return redirect("dashboard")
    else:
        subscription = Subscription.objects.get(id=pk)
        form = SubscriptionForm(instance=subscription)

    context = {
        "subscription": subscription,
        "form": form,
    }
    return render(request, "pages/update_customer.html", context)


def subscription_delete(pk):
    try:
        member = Subscription.objects.get(id=pk)
        member.delete()
        return redirect("/")
    except Subscription.DoesNotExist:
        return redirect("/")
