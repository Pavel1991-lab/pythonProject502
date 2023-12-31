
from django.core.mail import send_mail
from datetime import datetime, timedelta
from catalog.models import Product, MailingLog
from config import settings


def my_scheduled_job():
    current_time = datetime.now().time()
    current_date = datetime.now().date()
    all_product = Product.objects.all()

    for product in all_product:
        clients = product.clients.values_list('email', flat=True)  # получение списка email клиентов
        if product.mailing_time <= current_time and product.mailing_date == current_date and product.active == 'yes':
            try:
                    send_mail(
                        subject=product.topic,
                        message=product.description,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=clients  # передача списка email в качестве получателей
                    )

                    if product.period == 'daily':
                        product.mailing_date += timedelta(days=1)
                    elif product.period == 'weekly':
                        product.mailing_date += timedelta(days=7)
                    elif product.period == 'monthly':
                        product.mailing_date += timedelta(days=30)
                    product.save()
                    MailingLog.objects.create(response='ok', mailing = product)



            except Exception as e:
                MailingLog.objects.create(response=str(e))





