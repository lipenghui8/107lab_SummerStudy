from django.conf.urls import url
from .import views
urlpatterns=[
    #urlpatterns这个名字是固定的，类型也必须是列表
    url('^$',views.index),
    url('^(\d+)/$',views.detail),
]