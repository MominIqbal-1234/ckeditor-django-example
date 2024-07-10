from django.conf import settings
from django.core.mail import send_mail




def mail_sender(subject:str,message:str,reciver_mail):

    subject = subject
    message = message
    email_from = settings.EMAIL_HOST_USER
    reciver = [reciver_mail]
    send_mail(subject, message, email_from, reciver)
    return {
        "status":200,
        "message":"mail send"
    }
