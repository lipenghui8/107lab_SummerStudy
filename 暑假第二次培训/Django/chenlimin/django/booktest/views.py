# coding=utf-8
from django.shortcuts import render
# from django.http import HttpResponse
from .models import *
# Create your views here.


def index(request):
    # return HttpResponse('<h>hello world!</h>')
    # return render(request, 'booktest/index.html')
    list = BookInfo.objects.all()
    context = {'booklist': list}
    return render(request, 'booktest/index2.html', context)


def detail(request, id):
    list = BookInfo.objects.get(id=id).heroinfo_set.all()
    context = {'herolist': list}
    return render(request, 'booktest/detail.html', context)
