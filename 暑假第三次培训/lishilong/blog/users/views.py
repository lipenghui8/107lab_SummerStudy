import re
from users.models import User
from django.db import DatabaseError
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate
from django.views import View
from django.http.response import HttpResponseBadRequest, JsonResponse
from django.http.response import HttpResponse
from libs.captcha import captcha
from django_redis import get_redis_connection
from random import randint
from libs.yuntongxun.sms import CCP
from django.contrib.auth import logout
from home.models import ArticleCategory, Article
from django.core.paginator import Paginator,EmptyPage
from home.models import ArticleCategory
from utils.response_code import RETCODE
from django.shortcuts import redirect
import logging
logger = logging.getLogger('django')
# Create your views here.
class RegisterView(View):

    def get(self, request):

        return render(request, 'register.html')

    def post(self,request):

        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        smscode = request.POST.get('sms_code')

        if not all([mobile, password, password2, smscode]):
            return HttpResponseBadRequest('缺少必传参数')

        if not re.match(r'^1[3-9]\d{9}$', mobile):
            return HttpResponseBadRequest('手机号不符合规则')

        if not re.match(r'^[0-9A-Za-z]{8,20}$', password):
            return HttpResponseBadRequest('请输入8-20位的密码，密码是数字，字母')

        if password != password2:
            return HttpResponseBadRequest('两次密码不一致')

        redis_conn = get_redis_connection('default')
        redis_sms_code = redis_conn.get('sms:%s' % mobile)
        if redis_sms_code is None:
            return HttpResponseBadRequest('短信验证码已过期')
        if smscode != redis_sms_code.decode():
            return HttpResponseBadRequest('短信验证码不一致')

        try:
            user = User.objects.create_user(username=mobile, mobile=mobile, password=password)
        except DatabaseError as e:
            logger.error(e)
            return HttpResponseBadRequest('注册失败')

        from django.contrib.auth import login
        login(request, user)

        #return HttpResponse('注册成功，重定向到首页')
        response = redirect(reverse('home:index'))

        response.set_cookie('is_login', True)
        response.set_cookie('username', user.username, max_age=7*24*3600)

        return response


class ImageCodeView(View):

    def get(self, request):

        uuid = request.GET.get('uuid')
        if uuid is None:
            return HttpResponseBadRequest('没有传递uuid')
        text, image = captcha.captcha.generate_captcha()
        redis_conn = get_redis_connection('default')
        redis_conn.setex('img:%s' % uuid, 300, text)
        return HttpResponse(image, content_type='image/jpeg')
        pass

class SmsCodeView(View):

    def get(self,request):

        mobile = request.GET.get('mobile')
        image_code = request.GET.get('image_code')
        uuid = request.GET.get('uuid')

        if not all([mobile, image_code, uuid]):
            return JsonResponse({'code':RETCODE.NECESSARYPARAMERR, 'errsmg':'缺少必要参数'})

        redis_conn = get_redis_connection('default')
        redis_image_code = redis_conn.get('img:%s' % uuid)

        if redis_image_code is None:
            return JsonResponse({'code':RETCODE.IMAGECODEERR, 'errmsg':'图片验证码已过期'})

        try:
            redis_conn.delete('img:%s' % uuid)
        except Exception as e:
            logger.error(e)

        if redis_image_code.decode().lower() != image_code.lower():
            return JsonResponse({'code': RETCODE.IMAGECODEERR, 'errmsg': '图片验证码错误'})

        sms_code = '%06d' % randint(0, 999999)

        logger.info(sms_code)

        redis_conn.setex('sms:%s' % mobile, 300, sms_code)

        CCP().send_template_sms(mobile, [sms_code, 5], 1)

        return JsonResponse({'code': RETCODE.OK, 'errmsg': '发送短信成功'})


class LoginView(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):

        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        remember = request.POST.get('remember')


        if not re.match(r'^1[3-9]\d{9}$', mobile):
            return HttpResponseBadRequest('手机号不符合规则')


        if not re.match(r'^[0-9A-Za-z]{8,20}$', password):
            return HttpResponseBadRequest('密码不符合规则')


        user = authenticate(mobile=mobile, password=password)

        if user is None:
            return HttpResponseBadRequest('用户名或密码错误')


        from django.contrib.auth import login
        login(request, user)

        next_page = request.GET.get('next')
        if next_page:
            response = redirect(next_page)
        else:
            response = redirect(reverse('home:index'))



        if remember != 'on':

            request.session.set_expiry(0)

            response.set_cookie('is_login', True)
            response.set_cookie('username', user.username, max_age=14 * 24 * 3600)
        else:

            request.session.set_expiry(None)

            response.set_cookie('is_login', True)
            response.set_cookie('username', user.username, max_age=14 * 24 * 3600)

        return response

class LogoutView(View):

    def get(self, request):

        logout(request)

        response = redirect(reverse('home:index'))

        response.delete_cookie('is_login')

        return response



class ForgetPasswordView(View):

    def get(self, request):

        return render(request, 'forget_password.html')

    def post(self, request):
        # 接收参数
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        smscode = request.POST.get('sms_code')

        if not all([mobile, password, password2, smscode]):
            return HttpResponseBadRequest('参数不全')


        if not re.match(r'^1[3-9]\d{9}$', mobile):
            return HttpResponseBadRequest('手机号码不符合规则')


        if not re.match(r'^[0-9A-Za-z]{8,20}$', password):
            return HttpResponseBadRequest('密码不符合规则')


        if password != password2:
            return HttpResponseBadRequest('密码不一致')


        redis_conn = get_redis_connection('default')
        redis_sms_code = redis_conn.get('sms:%s' % mobile)
        if redis_sms_code is None:
            return HttpResponseBadRequest('短信验证码已过期')
        if smscode != redis_sms_code.decode():
            return HttpResponseBadRequest('短信验证码错误')


        try:
            user = User.objects.get(mobile=mobile)
        except User.DoesNotExist:

            try:
                User.objects.create_user(username=mobile, mobile=mobile, password=password)
            except Exception:
                return HttpResponseBadRequest('修改失败，请稍后再试')
        else:

            user.set_password(password)
            user.save()


        response = redirect(reverse('users:login'))

        return response


from django.contrib.auth.mixins import LoginRequiredMixin
class UserCenterView(LoginRequiredMixin,View):

    def get(self, request):

        user = request.user

        context = {
            'username': user.username,
            'mobile': user.mobile,
            'avatar': user.avatar.url if user.avatar else None,
            'user_desc': user.user_desc
        }
        return render(request, 'center.html', context=context)

    def post(self, request):

        user = request.user
        avatar = request.FILES.get('avatar')
        username = request.POST.get('username', user.username)
        user_desc = request.POST.get('desc', user.user_desc)


        try:
            user.username = username
            user.user_desc = user_desc
            if avatar:
                user.avatar = avatar
            user.save()
        except Exception as e:
            logger.error(e)
            return HttpResponseBadRequest('更新失败，请稍后再试')


        response = redirect(reverse('users:center'))

        response.set_cookie('username', user.username, max_age=14 * 24 * 3600)
        return response


class WriteBlogView(LoginRequiredMixin,View):

    def get(self, request):

        categories = ArticleCategory.objects.all()

        context = {
            'categories': categories
        }
        return render(request, 'write_blog.html', context=context)

    def post(self, request):

        avatar = request.FILES.get('avatar')
        title = request.POST.get('title')
        category_id = request.POST.get('category')
        tags = request.POST.get('tags')
        sumary = request.POST.get('sumary')
        content = request.POST.get('content')
        user = request.user


        if not all([avatar, title, category_id, sumary, content]):
            return HttpResponseBadRequest('参数不全')


        try:
            article_category = ArticleCategory.objects.get(id=category_id)
        except ArticleCategory.DoesNotExist:
            return HttpResponseBadRequest('没有此分类')




        try:
            article = Article.objects.create(
                author=user,
                avatar=avatar,
                category=article_category,
                tags=tags,
                title=title,
                sumary=sumary,
                content=content
            )
        except Exception as e:
            logger.error(e)
            return HttpResponseBadRequest('发布失败，请稍后再试')


        return redirect(reverse('home:index'))