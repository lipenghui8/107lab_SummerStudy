from django.urls import path

from .views import RegisterView, ImgCodeView, ForgetPasswordView
from .views import SmsCodeView, LoginView, LogoutView, UserCenterView
from .views import WriteBlogView
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('imagecode/', ImgCodeView.as_view(), name='imagecode'),
    path('smscode/', SmsCodeView.as_view(), name='imagecode'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('forgetpassword/', ForgetPasswordView.as_view(), name='forgetpassword'),
    path('center/', UserCenterView.as_view(), name='center'),
    path('writeblog/', WriteBlogView.as_view(),name='writeblog'),
]
