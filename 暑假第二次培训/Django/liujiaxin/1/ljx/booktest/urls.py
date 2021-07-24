from django.conf.urls import url

from . import views
urlpatterns = [
    url('index2/', views.index),
    url('(\\d+)/', views.detail),
]
