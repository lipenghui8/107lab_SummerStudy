from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def index(request):
    # return HttpResponse("Hello Django")
    # context = {'title':'django首页','list': range(10)}
    # return render(request,'booktext/index.html',context)
    list = BookInfo.objects.all()
    context = {'booklist':list}
    return render(request,'booktext/index2.html',context)

def details(request):
    list=BookInfo.objects.get(id=2).heroinfo_set.all()
    context={'herolist':list}
    return render(request,'booktext/details.html',context)