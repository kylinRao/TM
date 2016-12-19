#coding=utf-8
from celery.decorators import task
from .models import Todo
from datetime import datetime
from django.core.mail import send_mail,send_mass_mail
@task
def add(x, y):
    print 'add function'  
    return x + y
@task
def sendMail():
    mailMass=[]
    timenowMS=datetime.now().strftime("%H:%M")
    nowToDos=Todo.objects.filter(remind_time=timenowMS,remind_close=False)
    if nowToDos:
        for singleDo in nowToDos:
            mailsender=singleDo.remind_sender_email
            mailReceiver=singleDo.remind_receiver_email
            mailTitle=singleDo.remind_title
            mailContent=singleDo.remind_content
            message= (mailTitle,mailContent ,mailsender , [mailReceiver])    
            mailMass.append(message)
#            send_mail(mailTitle, mailContent, mailsender,    [mailReceiver], fail_silently=False)
        send_mass_mail(tuple(mailMass), fail_silently=False)
        try:
            
#            send_mass_mail(tuple(mailMass), fail_silently=False)
            print mailMass
            for singleDo in nowToDos:
                if singleDo.remind_only_once == True:
                    print singleDo.remind_only_once
                    singleDo.remind_close = True
                    singleDo.save()
        except:
            pass
            
    print nowToDos
    print datetime.now().strftime("%Y-%m-%d-%H:%M:%s")
