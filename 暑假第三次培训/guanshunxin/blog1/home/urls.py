from django.urls import path
from .views import IndexView,DetailView
urlpatterns=[
    path('',IndexView.as_view(),name='index'),
    path('detail/',DetailView.as_view(),name='detail'),
]