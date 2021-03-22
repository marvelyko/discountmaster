from celery import shared_task
from .models import EntryModel

@shared_task
def check():
    entries = EntryModel.objects.all()
    for entry in entries:
        print(entry.price)
        print(entry.site.price_function)
    print("checked")
    return "checked"