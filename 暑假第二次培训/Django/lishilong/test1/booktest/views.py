from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.
def index(request):
    #content = {'title':'django首页', 'list': range(10)}
    #return render(request, 'index.html', content)
    li = Bookinfo.objects.all()
    content = {'booklist': li}
    return render(request, 'index.html', content)
#def detial(request, id):
    #li = Bookinfo.objects.get(id=id).Heroinfo_set.all()
    #content={'herolist': li}
    #return render(request, 'detial.html', content)