#进行users子应用的视图路由
from django.urls import path
from users.views import RegisterView
from users.views import ImageCodeView
from users.views import SmsCodeView
from users.views import LoginView
from users.views import LogoutView
from users.views import ForgetPasswordView
from users.views import UserCenterView
from users.views import WriteBlogView

urlpatterns = [
    #path第一个参数路由
    #path第二个参数，视图函数
    path('register/', RegisterView.as_view(), name='register'),
    path('imagecode/', ImageCodeView.as_view(), name='imagecode'),
    path('smscode/', SmsCodeView.as_view(), name='smscode'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('forgetpassword/', ForgetPasswordView.as_view(), name='forgetpassword'),
    path('center/', UserCenterView.as_view(),name='center'),
    path('writeblog/', WriteBlogView.as_view(),name='writeblog'),
]
