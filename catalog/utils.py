import psycopg2
from django.core.mail import send_mail

from catalog.classDB_meneger_ import DBManager
from django.core.mail import send_mail
from datetime import datetime

from catalog.models import Product, Client
from config import settings


def my_scheduled_job():
    current_time = datetime.now().time()
    current_date = datetime.now().date()
    all_product = Product.objects.all()
    for product in all_product:
        clients = product.clients.all()
        for client in clients:
            if product.mailing_time <= current_time and product.mailing_date == current_date:
                send_mail(
                    subject=product.topic,
                    message=product.description,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[client.email]
                )

