
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *


def index(request):
    list = BookInfo.objects.all()
    context = {'booklist': list}
    return render(request, 'booktest/index2.html', context)


def detail(request, id):
    list = BookInfo.objects.get(id=id).heroinfo_set.all()
    context = {'herolist': list}
    return render(request, 'booktest/detail.html', context)

