from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Users, Article
import random
from django.utils import timezone


def superUser(request):
    adminmessage = '请输入用户名'
    return render(request, 'admin/admin.html', locals())


def superUserCheck(request):
    adminmessage = '请输入用户名'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('username:',username)
        print('password:',password)
        supername = Users.userM.get(userNub=1)
        try:
            name = Users.userM.get(username=username)
            print(name.userNub)
            if name.userNub == "1":
                request.session['is_signs'] = True
                return redirect('/login/adminhp', locals())
                # return HttpResponse(111111)
            else:
                print(name.userNub)
                adminmessage = '用户权限不够'
                return render(request, 'admin/admin.html', locals())
        except:
            adminMessage = '请输入正确的用户名'
            return render(request, 'admin/admin.html', locals())


def superUserHp(request):
    articles = Article.articleM.all()
    users = Users.userM.all()
    for user in users:
        if user.userNub == '0':
            user.userNub = '普通用户'
        elif user.userNub == '1':
            user.userNub = '超级用户'
    return render(request, 'admin/adminhp.html', locals())


def userDel(request):
    userId = request.GET.get('user_id')
    Users.userM.filter(id=userId).delete()
    return redirect(superUserHp)


def userModify(request, userId,userNub):
    Users.userM.filter(id=userId).update(userNub=userNub)
    return redirect(superUserHp)


def adminArticle(request):
    return render(request, 'admin/adminArticleAdd.html', locals())


def adminArticleAdd(request):
    title = request.GET.get("title")
    name = request.GET.get("name")
    content = request.GET.get("content")
    date = timezone.now()
    Article.articleM.create(title=title,articleName=name,content=content,publishDate=date)
    return redirect(superUserHp)


