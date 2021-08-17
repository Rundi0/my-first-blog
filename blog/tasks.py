from celery.app import shared_task

from mysite.celery import app
from blog.postmark import send_mail_simple

@shared_task
def add(x, y):
    return x + y

@shared_task
def celery_send_mail(to_mail : list, title : str, text : str):
    return send_mail_simple(to_mail, title, text)