
from django.contrib import staticfiles
from django.conf.urls import url
from django.urls import path
from . import views,superuser
 


urlpatterns = [
    
    # path('logon',views.logon),
    # path('login',viewsLogin.login),
    # path('signin',viewsLogin.signin),
    # path('loginJudge',viewsLogin.loginJudge),
    # path('signins',viewsLogin.signins),
    # path('user/<slug:username>/',views.userPage),
    # path('logout',views.logout),
    # path('article/<slug:articleId>',views.articlePage),
    path('login/admin',superuser.superUser),
    path('login/adminhp',superuser.superUserHp),
    path('login/superUserCheck',superuser.superUserCheck),
    path('login/superUserCheck/userdel/',superuser.userDel),
    path('login/superUserCheck/userModify/<str:userId>?<str:userNub>',superuser.userModify),
    path('login/superUserCheck/articleAdd',superuser.adminArticle),
    path('login/superUserCheck/adminArticleAdd',superuser.adminArticleAdd),
    path('news',views.news),
    path('newsContent',views.newsContent),
    path('login',views.login),
    path('csrf',views.csrf),
    path('signin',views.signin),
    path('logout',views.logout),
    path('addPage',views.addPage)
]

