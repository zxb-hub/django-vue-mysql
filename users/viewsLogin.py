from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Users,Article
import random
from django.http import JsonResponse
import json


def login(request):
    return render(request,'login.html')

def signin(request):
    return render(request,'signin.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            users = Users.userM.get(username=username)
            print(users.password)
            print(password)
            if password == users.password:
                messageL = 0
                return messageL
            else:
                return messageL = 1
        except:
            return messageL = 2
    return JsonResponse(messageL)



def signins(request):
        if request.method=='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            phone = request.POST.get('phone')
            users = Users.userM.filter(username = username)
            userNub=''
            
                user = Users(username=username, password=password,
                            phone=phone,userNub=userNub)
                user.save()
                request.session['username'] = username
                request.session['password'] = password
                return render(request, 'hp.html', locals())
        return render(request,'signin.html',locals())
