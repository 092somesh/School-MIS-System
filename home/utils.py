import time
from .models import Student
from django.core.mail import send_mail
from django.conf import settings
def send_email_to_client():
    subject ="this email is from django"
    message ="this is a test msg for django"
    from_email=settings.EMAIL_HOST_USER
    recipient_list=["someshh0628@gmail.com"]
    send_mail(subject,message,from_email,recipient_list)
 
def run_this_function():
    print("Function started")
    time.sleep(5)
    print("funtion executed")