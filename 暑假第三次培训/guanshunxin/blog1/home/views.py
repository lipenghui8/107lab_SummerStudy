from django.shortcuts import render
from django.views import View
from .models import ArticleCategory,Article
from django.http.response import HttpResponseNotFound
# Create your views here.
class IndexView(View):
    def get(self,request):
        #1获取所有信息
        categories=ArticleCategory.objects.all()
        #2接受用户点击的信息
        cat_id=request.GET.get('cat_id',1)
        #3根据分类id进行分类的查询
        try:
            category=ArticleCategory.objects.get(id=cat_id)
        except ArticleCategory.DoesNotExist:
            return HttpResponseNotFound('没有此分类')
        #4获取分页参数
        page_num=request.GET.get('page_num',1)
        page_size=request.GET.get('page_size',10)
        #5根据分类信息查询文章数据
        articles=Article.objects.filter(category=category)
        #6创建分页器
        from django.core.paginator import Paginator,EmptyPage
        paginator=Paginator(articles,per_page=page_size)
        #7进行分页处理
        try:
            page_articles=paginator.page(page_num)
        except EmptyPage:
            return HttpResponseNotFound('empty page')
        #总页数
        total_page=paginator.num_pages
        #8组织数据传递给模板
        context={
            'categories':categories,
            'category':category,
            'articles':page_articles,
            'page_size':page_size,
            'total_page':total_page,
            'page_num':page_num,

        }
        return render(request,'index.html',context=context)
from .models import Comment
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
class DetailView(View):
    def get(self,request):
        #1接收文章id信息
        id=request.GET.get('id')
        #2根据文章id进行文章数据的查询
        try:
            article=Article.objects.get(id=id)
        except Article.DoesNotExist:
            return render(request,'404.html')
        else:
            article.total_views+=1
            article.save()

        #3查询分类数据
        categories = ArticleCategory.objects.all()
        hot_article=Article.objects.order_by('-total_views')[:9]
        #获取分页请求参数
        page_size=request.GET.get('page_size',10)
        page_num=request.GET.get('page_num',1)
        #根据文章信息查询评论数据
        comments=Comment.objects.filter(article=article).order_by('-created')
        #获取评论总数
        total_count=comments.count()
        #创建分页器
        from django.core.paginator import Paginator,EmptyPage
        paginator=Paginator(comments,page_size)
        # 进行分页处理
        try:
            page_comments=paginator.page(page_num)
        except EmptyPage:
            return HttpResponseNotFound('empty page')
        #总页数
        total_page=paginator.num_pages
        #4组织模板数据
        context={
            'categories':categories,
            'category':article.category,
            'article':article,
            'hot_articles':hot_article,
            'total_count':total_count,
            'comments':page_comments,
            'page_size':page_size,
            'total_page':total_page,
            'page_num':page_num
        }
        return render(request,'detail.html',context=context)
    def post(self,request):
        #1接收用户信息
        user=request.user
        #判断用户是否登录
        if user and user.is_authenticated:
            #登录用户可以接收form数据
                #接受评论数据
            id=request.POST.get('id')
            content=request.POST.get('content')
                #验证文章是否存在
            try:
                article=Article.objects.get(id=id)
            except Article.DoesNotExist:
                return HttpResponseNotFound('没有此文章')
                #保存评论数据
            Comment.objects.create(
                content=content,
                article=article,
                user=user
            )
                #修改文章评论数量
            article.comments_count+=1
            article.save()
            path=reverse('home:detail')+'?id={}'.format(article.id)
            return redirect(path)
        else:
            return redirect(reverse('users:login'))

