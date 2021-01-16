from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Users, Article, UserToken
from django.core import serializers
import random
import json
import math
from django.http import JsonResponse
from django.middleware.csrf import get_token
from users import models
from django.contrib.auth.hashers import make_password, check_password


def csrf(request):
    token = get_token(request)
    print(token)
    return HttpResponse(json.dumps({'token': token}), content_type="application/x-www-form-urlencoded;charset=utf-8")


def login(request):
    if request.method == 'POST':
        print(request.body)
        print(request.POST)
        req = json.loads(request.body)
        username = req.get('username')
        password = req.get('password')
        print('姓名', username)
        print('密码:', password)
        user = Users.userM.filter(username=username, password=password).first()
        message = {"msg": '', 'token': '', 'name': '', 'msgid': ''}
        print(message)
        if user:
            token = make_password(username + password)
            UserToken.tokenM.update_or_create(
                username=username, defaults={"token": token})
            message["msgid"] = 200
            message["msg"] = "登入成功"
            message["token"] = token
            message["name"] = user.username
        else:
            message['msg'] = 404
            message['msg'] = '登陆失败'
            message['token'] = None
            message["name"] = None
        return JsonResponse(message)


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        print("username:", username)
        password = request.POST.get("password")
        print("password:", password)
        phone = request.POST.get("phone")
        print("phone", phone)
        message = {"msg": '','token': '','name': ''}
        userNub = 0
        users = Users.userM.filter(username=username)
        print("users:", users)
        p = Users.userM.filter(phone=phone)
        print("phone:", p)
        if users.count() != 0:
            message['msg'] = 1  # 返回1 用户名已存在
            return JsonResponse(message)
        elif p.count() != 0:
            message['msg'] = 2  # 返回2 电话号已存在
            return JsonResponse(message)
        else:
            user = Users(username=username, password=password,
                         phone=phone, userNub=userNub)
            user.save()
            token = make_password(username + password)
            UserToken.tokenM.update_or_create(
                username=username, defaults={"token": token})
            message["token"] = token
            message['msg'] = 0
            message["name"] = username
            return JsonResponse(message)


def logout(request):
    if request.method == 'GET':
        # user = request.GET.get('username')
        # print(request.body)
        # print('get',request.GET.)
        # print('get',request.GET.get)
        # print('username:',user)
        username = UserToken.tokenM.get()
        username.delete()
        msg = '1'
    return HttpResponse(msg)


def news(request):
    if request.method == 'GET':
        news = json.loads(serializers.serialize("json", Article.articleM.filter().all()))
        
        news = list(news)
        return JsonResponse(news, safe=False)
        # return HttpResponse(news)


def addPage(request):
    if request.method == 'GET':
        
        news = Article.articleM.all()
        # print(news)
        totalCount = len(news)
        # totalDate['totalCount'] = totalCount
        # print('totalCount', totalCount)
        totalPage = math.ceil(totalCount/5)
        # totalDate['totalPage'] = totalPage
        # print('totalPage', totalPage)
        page = request.GET.get("pageId")
        # print('pages:',request.GET.)
        # print('page:',page)
        page = int(page)
        pages = page + 5
        newPage =json.loads(serializers.serialize("json",  Article.articleM.all()[page:pages]))
        # newPage =json.loads(serializers.serialize("json",  Article.articleM.all()))
        # totalDate['newPage'] = newPage
        # print('newPage:',newPage)
        totalDate = {'totalCount': totalCount, 'totalPage': totalPage, 'newPage': newPage}
        return JsonResponse(totalDate)
# <bound method MultiValueDict.get of <QueryDict: {'user': ['zxb']}>>
#  <bound method MultiValueDict.get of <QueryDict: {'newsId': ['1']}>>


def newsContent(request):
    if request.method == 'GET':
        # print("前端传入",request.GET.filter('newsId'))
        id = request.GET.get('newsId')
        contentDate = Article.articleM.filter(articleId=id)
            # print('1-1:',content[0].articleId)
            # print('1-2:',content)
            # content.append([contentDate[0].articleId,contentDate[0].title,contentDate[0].articleName,contentDate[0].content,contentDate[0].publishDate])
            # content.append(Article.articleM.filter(articleId=i))
        print('get:', request.GET.get)
        # print(id)
        # content = Article.articleM.values().filter(articleId=id)
        print('content的值:', contentDate)
        # print('所有值:',Article.articleM.filter(articleId=2))
        # print('content的值:',content.title)
        # contents['data'] = content
        # print("content数据类型",type(content))
        content =json.loads(serializers.serialize("json",contentDate))
        # contents['data'] = json.loads(serializers.serialize("json",content))
        # content =json.loads(serializers.serialize("json",content))
    return JsonResponse(content, safe=False)
        # return HttpResponse(json.dumps(contents))



    