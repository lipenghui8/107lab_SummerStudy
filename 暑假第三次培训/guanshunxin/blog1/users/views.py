from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
import sys,re
sys.path.append("C:\\Users\\DELL\\Desktop\\新建文件夹 (11)\\blog1\\users")
sys.path.append("C:\\Users\\DELL\\Desktop\\新建文件夹 (11)\\blog1\\home\\")
from django.db import DatabaseError
from django.http.response import HttpResponseBadRequest

from .models import User
# Create your views here.
from django.views import View
class RegisterView(View):
    def get(self,request):
        return render(request,'register.html')
    def post(self,request):
        mobile=request.POST.get('mobile')
        password=request.POST.get('password')
        password2=request.POST.get('password2')
        smscode=request.POST.get('sms_code')

        if not all([mobile,password,password2,smscode]):
            return HttpResponseBadRequest('缺少必要参数')
        if not re.match(r'^1[3-9]\d{9}$',mobile):
            return HttpResponseBadRequest('手机号不符合规则')
        if not re.match(r'^[0-9a-zA-Z]{8,20}$',password):
            return HttpResponseBadRequest('请输入8-20位密码，密码是字母和数字')
        if password!=password2:
            return HttpResponseBadRequest('两次密码不一致')
        redis_coon=get_redis_connection('default')
        redis_sms_code=redis_coon.get('sms:%s'%mobile)
        if redis_sms_code is None:
            return HttpResponseBadRequest('短信验证码已过期')
        if smscode!=redis_sms_code.decode():
            return HttpResponseBadRequest('短信验证码不一致')
        try:
            user=User.objects.create_user(username=mobile,
                                      mobile=mobile,
                                      password=password)
        except DatabaseError as e:
            logger.error(e)
            return HttpResponseBadRequest('注册失败')
        from django.contrib.auth import login
        login(request,user)
        # return HttpResponse('注册成功')
        response=redirect(reverse('home:index'))
        response.set_cookie('is_login',True)
        response.set_cookie('username',user.username,max_age=7*24*3600)
        return response








from django.http.response import HttpResponseBadRequest
from captcha import captcha
from random import randint
from django_redis import get_redis_connection
from django.http import HttpResponse
class ImgCodeView(View):
    def get(self,request):
        uuid=request.GET.get('uuid')
        if uuid is None:
            return HttpResponseBadRequest('没有传递uuid')
        text,image= captcha.generate_captcha()
        redis_coon=get_redis_connection('default')
        redis_coon.setex('img:%s'%uuid,300,text)
        return HttpResponse(image,content_type='image/jpeg')
from django.http.response import JsonResponse
from response_code import RETCODE
import logging
from sms import CCP
logger=logging.getLogger('django')

class SmsCodeView(View):
    def get(self,request):
        mobile=request.GET.get('mobile')
        image_code=request.GET.get('image_code')
        uuid=request.GET.get('uuid')
        if not all([mobile,image_code,uuid]):
            return JsonResponse({'code':RETCODE.NECESSARYPARAMERR,'errmsg':'缺少参数'})
        redis_coon=get_redis_connection('default')
        redis_image_code=redis_coon.get('img:%s'%uuid)
        if redis_image_code is None:
            return JsonResponse({'code':RETCODE.IMAGECODEERR,'errmsg':'图片验证码过期'})
        try:
            redis_coon.delete('img:%s'%uuid)
        except Exception as e:
            logger.error(e)
        if redis_image_code.decode().lower()!=image_code.lower():
            return JsonResponse({'code':RETCODE.IMAGECODEERR,'errmsg':'图片验证码错误'})
        sms_code='%06d'%randint(0,999999)
        logger.info(sms_code)
        redis_coon.setex('sms:%s'%mobile,300,sms_code)
        CCP().send_template_sms(mobile,[sms_code,5],1)
        return JsonResponse({'code':RETCODE.OK,'errmsg':'短信发送成功'})

class LoginView(View):
     def get(self,request):
         return render(request,'login.html')
     def post(self,request):
         #1接收参数
         mobile=request.POST.get('mobile')
         password=request.POST.get('password')
         remember=request.POST.get('remember')

         #2参数验证
         if not re.match(r'^1[3-9]\d{9}$',mobile):
             return HttpResponseBadRequest('手机号不符合规则')
         if not re.match(r'^[a-zA-Z0-9]{8,20}$',password):
             return HttpResponseBadRequest('密码不符合规范')
         #3用户登录
         from django.contrib.auth import authenticate
         user=authenticate(mobile=mobile,password=password)
         if user is None:
             return HttpResponseBadRequest('用户名或密码错误')
         #4状态保持
         from django.contrib.auth import login
         login(request,user)
         next_page=request.GET.get('next')
         if next_page:
             response=redirect(next_page)
         else:
             response=redirect(reverse('home:index'))
         #5根据用户选择是否记住登录状态
         if remember !='on':
             request.session.set_expiry(0)
             response.set_cookie('is_login',True)
             response.set_cookie('username',user.username,max_age=14*24*3600)

         else:
             request.session.set_expiry(None)
             response.set_cookie('is_login', True,max_age=14*24*3600)
             response.set_cookie('username', user.username, max_age=14 * 24 * 3600)
         #6为首页显示设置cookie
         #7返回响应
         return response
from django.contrib.auth import logout
class LogoutView(View):
    def get(self,request):
        logout(request)
        response=redirect(reverse('home:index'))
        response.delete_cookie('is_login')
        return response

class ForgetPasswordView(View):
    def get(self,request):
        return render(request,'forget_password.html')
    def post(self,requset):
        mobile=requset.POST.get('mobile')
        password=requset.POST.get('password')
        password2=requset.POST.get('password2')
        smscode=requset.POST.get('sms_code')
        if not all([mobile, password, password2, smscode]):
            return HttpResponseBadRequest('缺少必要参数')
        if not re.match(r'^1[3-9]\d{9}$', mobile):
            return HttpResponseBadRequest('手机号不符合规则')
        if not re.match(r'^[0-9a-zA-Z]{8,20}$', password):
            return HttpResponseBadRequest('请输入8-20位密码，密码是字母和数字')
        if password != password2:
            return HttpResponseBadRequest('两次密码不一致')
        redis_coon = get_redis_connection('default')
        redis_sms_code = redis_coon.get('sms:%s' % mobile)
        if redis_sms_code is None:
            return HttpResponseBadRequest('短信验证码已过期')
        if smscode != redis_sms_code.decode():
            return HttpResponseBadRequest('短信验证码不一致')
        try:
            user=User.objects.get(mobile=mobile)
        except User.DoesNotExist:
            try:
                User.objects.create_user(username=mobile,
                                         mobile=mobile,
                                         password=password)
            except Exception:
                return HttpResponseBadRequest('修改失败')
        else:
            user.set_password(password)
            user.save()
        response=redirect(reverse('users:login'))
        return response
from django.contrib.auth.mixins import LoginRequiredMixin
class UserCenterView(LoginRequiredMixin,View):
    def get(self,request):
        user=request.user
        context={
            'username':user.username,
            'mobile':user.mobile,
            'avatar':user.avatar.url if user.avatar else None,
            'user_desc':user.user_desc,
        }
        return render(request,'center.html',context=context)
    def post(self,request):
        user=request.user
        username=request.POST.get('username',user.username)
        user_desc=request.POST.get('desc',user.user_desc)
        avatar=request.FILES.get('avatar')
        try:
            user.username=username
            user.user_desc=user_desc
            if avatar:
                user.avatar=avatar
            user.save()
        except Exception as e:
            logger.error(e)
            return HttpResponseBadRequest('修改失败')
        response=redirect(reverse('users:center'))
        response.set_cookie('username',user.username,max_age=24*14*3600)
        return response
from home.models import ArticleCategory,Article
class WriteBlogView(LoginRequiredMixin,View):
    def get(self,request):
        categories=ArticleCategory.objects.all()

        context={
            'categories':categories
        }
        return render(request,'write_blog.html',context=context)
    def post(self,request):
        #接收数据
        avatar=request.FILES.get('avatar')
        title=request.POST.get('title')
        category_id=request.POST.get('category')
        tags=request.POST.get('tags')
        sumary=request.POST.get('sumary')
        content=request.POST.get('content')
        user=request.user
        #验证数据
        #参数是否齐全
        if not all([avatar,title,category_id,sumary,content]):
            return HttpResponseBadRequest('参数不全')
        try:
            category=ArticleCategory.objects.get(id=category_id)
        except ArticleCategory.DoesNotExist:
            return HttpResponseBadRequest('没有此分类')

        #数据入库
        try:
            article=Article.objects.create(
                author=user,
                title=title,
                avatar=avatar,
                category=category,
                tags=tags,
                sumary=sumary,
                content=content,
            )

        except Exception as e:
            logger.error(e)
            return HttpResponseBadRequest('发布失败')
        #跳转到指定页面
        return redirect(reverse('home:index'))
