from django.contrib import admin
from .models import * #也可以写成myblog.models
# Register your models here.

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','title','pub_date']
class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id','name','content','gender','book']
#注册模型类，后台可以进行管理
admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo)
