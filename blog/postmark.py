from postmarker.core import PostmarkClient
from postmarker.exceptions import ClientError
from django.core.mail import send_mail

from mysite.settings import PM_API_KEY, MAIL_ADDRESS, POSTMARK

def send_mail_postmark(to_mail : list, title : str, text : str):
    postmark = PostmarkClient(PM_API_KEY)
    postmark.emails.send(
        From=MAIL_ADDRESS,
        To=to_mail[0],
        Subject=title,
        HtmlBody=text
    )

def send_mail_simple(to_mail : list, title : str, text : str):
    try:
        smtp_send_mail(to_mail, title, text)
    except ClientError as e:
        print(e.error_code)
        return "ERROR! Incorect date!"
    
    return "Successful send mail!"

def smtp_send_mail(to_mails : list, title : str, body : str):
    send_mail(title, body,MAIL_ADDRESS, to_mails, fail_silently=False)