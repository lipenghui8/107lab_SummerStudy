from django.contrib import admin
from bookuse.models import *
# Register y


class BookInfoadmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date']


class Peopleadmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'PersonInfo', 'gender', 'book']


admin.site.register(BookInfo, BookInfoadmin)
admin.site.register(People, Peopleadmin)
