from django.db import models
from django.utils import timezone 

class Users(models.Model):
    userM   = models.Manager()
    username=models.CharField(max_length=20,db_column='username',blank=False)
    userNub=models.CharField(max_length=20,db_column='userNub',default=0)
    password=models.CharField(max_length=20,db_column='password',blank=False)
    phone   = models.CharField(max_length=30,db_column='phone',blank=False)
    date = models.DateTimeField(default = timezone.now)

    class Meta:
        db_table="users"#定义数据表名，推荐小写
        ordering=['username']#对象默认排序字段，获取对象列表时使用


    def __str__(self):
        return self.username


class Article(models.Model):
    articleM = models.Manager()
    articleId = models.AutoField(primary_key=True)
    title = models.TextField()#文章题目
    articleName=models.TextField()#作者名
    content = models.TextField()#上传文章主要内容
    publishDate = models.DateTimeField(default=timezone.now)#上传时间
   
    class Meta:
        ordering= ['-publishDate']#设置文章显示顺序以publishDate为依据
    def __str__(self):
        return self.title

class UserToken(models.Model):
    tokenM = models.Manager()
    username = models.CharField(db_column='username',max_length=32)
    token = models.CharField(db_column='token', max_length=300)
