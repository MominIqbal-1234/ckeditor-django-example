# views.py

from django.shortcuts import render, redirect,HttpResponse
from django.http import JsonResponse
from .forms import UserInfoForm
from app.sendmail import mail_sender
from app import models

def create_article(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/') 
    else:
        form = UserInfoForm()
    
    return render(request, 'create_article.html', {'form': form})




def mymail(request):

    subject = "This Mail"
    message = " this is mail  " 
    reciver_mail = ""
    res = mail_sender(subject,message,reciver_mail)
    print(res)
    return JsonResponse(res)





    