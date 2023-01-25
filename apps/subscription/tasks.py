from django.utils import timezone
from django.db.models import F
from django.core.mail import EmailMessage

from .models import Subscription

def send_expiration_email():
    today = timezone.now().date()
    subject = "Your subscription expiring soon !!!!!"
    body = """
            Your subscripton is expiring soon. Please renew subscription timely.
            Thank You!!!
            """
    for subscription in Subscription.objects.annotate(diff=F('to_date') - today):
        if subscription.diff.days <= 5:
            email = EmailMessage(subject, body, to=[subscription.customer.email])
            email.send()    
            print("send mail successfully")
#     qs=Subscription.objects.filter(to_date__range=[today,today_plus_five])

#     for subscription in Subscription.objects.filter(to_date__lte=(today+timezone.timedelta(day=5)).date):
        


                