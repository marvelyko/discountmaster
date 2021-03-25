from celery import shared_task
from .models import EntryModel

def send_mail(email,url,price):
    return None

@shared_task
def check():
    entries = EntryModel.objects.all()
    for entry in entries:
        wanted_price = entry.price
        current_price = entry.site.price_function
        
        if current_price < wanted_price:
            send_mail(entry.email,entry.url,untry.price)
            #entry.delete()

    return "checked"
