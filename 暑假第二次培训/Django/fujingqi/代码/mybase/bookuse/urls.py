from django.urls import path
from django.conf.urls import url
from . import views

import bookuse.views
urlpatterns = [
    path('', views.index, name='index'),
    url('(\\d+)/', views.details),
]
