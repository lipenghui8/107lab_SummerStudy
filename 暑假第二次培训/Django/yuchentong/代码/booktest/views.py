from django.shortcuts import  render
from django.shortcuts import render
from django.http import  HttpResponse
from models import*
# Create your views here.
def index(requst):
    #return HttpResponse('<h1>helloworld</h1>')
    #context={'title':'django首页','list':range(10)}
    #return render(requst,'booktest/index.html',context)
    list=BookInfo.objects.all()
    context={'booklist':list}
    return render(requst,'booktest/index2.html',context)
def detail(request,id):
    list=BookInfo.objects.get(id=id).heroinfo_set.all()
    context={'herolist':list}
    return reder(request,'booktest/detail.html',context)