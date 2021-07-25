from django.contrib import admin
from .models import *
# Register your models here.

class BookinfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub_data']
class HeroinfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'content', 'gender', 'book']

admin.site.register(Bookinfo, BookinfoAdmin)
admin.site.register(Heroinfo, HeroinfoAdmin)
