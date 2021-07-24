from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *


def index(request):

    list = BookInfo.objects.all()
    context = {'booklist': list}
    return render(request, 'bookuse/index2.html', context)


def details(request, id):
    list = BookInfo.objects.get(id=id).people_set.all()
    context = {'Personlist': list}
    return render(request, 'bookuse/details.html', context)
