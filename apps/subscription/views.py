from django.contrib import messages
from email.message import EmailMessage
import smtplib
import ssl
from django.shortcuts import render, redirect
from apps.subscription.forms import SubscriptionForm
from apps.subscription.models import Subscription
from datetime import datetime, timedelta


def subscription_dashboard(request):
    fil = {}
    if request.method == "POST":
        fil["status"] = request.POST.get("status")
    enquires = Subscription.objects.filter(**fil)
    context = {"enquires": enquires}

    return render(request, "pages/subscription/subdashboard.html", context)


def subscription_create(request):
    context = dict()
    if request.method == "POST":
        form = SubscriptionForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("list-subscription")
    else:
        form = SubscriptionForm()
    context["form"] = form
    return render(request, "pages/subscription/add_subscription.html", context)


def subscription_update(request, pk):
    if request.method == "POST":
        subscription = Subscription.objects.get(id=pk)
        form = SubscriptionForm(request.POST, request.FILES, instance=subscription)
        if form.is_valid():
            form.save()
            messages.success(request, "update successfully")
            return redirect("list-subscription")
    else:
        subscription = Subscription.objects.get(id=pk)
        form = SubscriptionForm(instance=subscription)

    context = {
        "subscription": subscription,
        "form": form,
    }
    return render(request, "pages/subscription/update.html", context)


def subscription_delete(request, pk):
    member = Subscription.objects.get(id=pk)
    member.delete()
    return redirect("list-subscription")


def sendmail(request):
    email_sender = "mission.sharma101@gmail.com"
    email_password = "zapgldcllkdallwb"
    subs = Subscription.objects.all()
    for i in subs:
        start_date = i.from_date
        to_date = i.to_date
        differ = to_date - start_date
        print(differ)
        print(i.status)
        x = timedelta(days=5)
        if differ <= x and i.status == "paid":
            email_receiver = i.customer.email
    subject = "Subscription time is going to timeout!!!"
    body = """"
            Your subscripton is running out so please buy subscription at timely.
            Thank You!!!
            """
    em = EmailMessage()
    em["from"] = email_sender
    em["to"] = email_receiver
    em["subject"] = subject
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
        messages.success(request, "send mail successfully")
        return redirect("/")
