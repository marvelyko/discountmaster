from celery import shared_task
from .models import EntryModel
import smtplib

def send_mail(email,url,price):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('karlo.tevzadze.1@iliauni.edu.ge', 'hmhltdcchueknufd')

    subject = 'Price fell down'
    body = f'''
    Url: {url}
    Price : {price}
    '''

    msg = f'Subject: {subject}\n\n{body}'

    server.sendmail(
        'karlo.tevzadze.1@iliauni.edu.ge',
        email,
        msg
    )
    print("Email Sent")

    server.quit()

@shared_task
def check():
    entries = EntryModel.objects.all()
    for entry in entries:
        wanted_price = entry.price
        function_text = entry.site.price_function
        
        exec(function_text,globals())

        current_price = f(entry.url)

        if current_price < wanted_price:
            send_mail(entry.email, entry.url, entry.price)
            entry.delete()

    return "checked"
