from django.contrib import admin
from .models import Users
from .models import Article
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('articleId','title','articleName','publishDate')


admin.site.register(Users),
admin.site.register(Article,ArticleAdmin)
