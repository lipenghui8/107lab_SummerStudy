from django.db import models
from django.utils import timezone
# Create your models here.
class ArticleCategory(models.Model):
    title=models.CharField(max_length=100,blank=True)
    created=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title
    class Meta:
        db_table='tb_category'
        verbose_name='类别管理'
        verbose_name_plural=verbose_name
from django.utils import timezone
from users.models import User
class Article(models.Model):
    #作者
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    #标题图
    avatar=models.ImageField(upload_to='article/%Y%m%d/',blank=True)
    #标题
    title=models.CharField(max_length=20,blank=True)
    #分类
    category=models.ForeignKey(ArticleCategory,null=True,blank=True,on_delete=models.CASCADE,related_name='article')
    #标签
    tags=models.CharField(max_length=20,blank=True)
    #摘要信息
    sumary=models.CharField(max_length=20,blank=False)
    #文章正文
    content=models.TextField()
    #浏览量
    total_views=models.PositiveIntegerField(default=0)
    #评论量
    comments_count=models.PositiveIntegerField(default=0)
    #文章创建时间
    created=models.DateTimeField(default=timezone.now)
    #文章修改时间
    updated=models.DateTimeField(auto_now=True)
    #修改表名以及admin展示的配置信息
    class Meta:
        db_table='tb_article'
        ordering=('-created',)
        verbose_name='文章管理'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.title


class Comment(models.Model):
    #评论内容
    content=models.TextField()
    #评论的文章
    article=models.ForeignKey(Article,on_delete=models.SET_NULL,null=True)
    #评论的用户
    user=models.ForeignKey('users.User',on_delete=models.SET_NULL,null=True)
    #评论的时间
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.article.title
    class Meta:
        db_table='tb_comment'
        verbose_name='评论管理'
        verbose_name_plural=verbose_name

