from django.contrib import admin
from .models import *
# Register your models here.
class BookInfoAdmin(admin.ModelAdmin):
    list_disAdplay = ['id','title','pub_date']
class HeroInfomin(admin.ModelAdmin):
    list_display = ['id','name','content','gender','book']
admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)
