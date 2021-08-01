from django.shortcuts import render
from django.http import HttpResponse
from .models import BookInfo
# Create your views here.
def index(request): #request必须有，它封装的是所有请求信息
    #必须返回一个相应对象HttpResponse
    #return HttpResponse('hello world')
    #context={'title':'django首页','list':range(10)}
    #return  render(request,'newapp/index.html',context)
    list=BookInfo.objects.all()
    context={'booklist':list}
    return render(request,'newapp/index.html',context)

def detail(request,id):
    list=BookInfo.objects.get(id=id).heroinfo_set.all()
    context={'herolist':list}
    return render(request,'newapp/detail.html',context)
