from django.shortcuts import render
from django.views import View
from home.models import ArticleCategory, Article
from django.http import HttpResponseNotFound
# Create your views here.
class IndexView(View):
    def get(self, request):
        categories = ArticleCategory.objects.all()
        cat_id = request.GET.get('cat_id', 1)
        try:
            category = ArticleCategory.objects.get(id=cat_id)
        except ArticleCategory.DoesNotExist:
            return HttpResponseNotFound('没有此分类')

        page_num = request.GET.get('page_num')
        page_size = request.GET.get('page_size', 10)
        articles = Article.objects.filter(category=category)
        from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
        paginator = Paginator(articles, per_page=page_size)
        try:
            page_articles = paginator.page(page_num)
        except PageNotAnInteger:
            page_articles = paginator.page(1)
        except EmptyPage:
            return HttpResponseNotFound('empty page')

        total_page = paginator.num_pages
        context = {
            'categories': categories,
            'category': category,
            'articles': page_articles,
            'page_size': page_size,
            'total_page': total_page,
            'page_num': page_num,
        }
        return render(request, 'index.html', context=context)


class DetailView(View):
    def get(self, request):
        id = request.GET.get('id')
        try:
            article = Article.objects.get(id=id)
        except Article.DoesNotExist:
            return render(request, '404.html')
        else:
            article.total_views += 1
            article.save()
        categories = ArticleCategory.objects.all()
        hot_articles = Article.objects.order_by('_total_views')[:9]
        context = {
            'categories': categories,
            'article': article,
            'category': article.category,
            'hot_articles': hot_articles,

        }

        return render(request, 'detail.html', context=context)