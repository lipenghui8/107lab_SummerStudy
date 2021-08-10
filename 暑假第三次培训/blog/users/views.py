from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import render
# Create your views here.
from django.views import View
import re
from users.models import User
from django.db import DatabaseError
class RegisterView(View):
    """用户注册"""

    def get(self, request):
        """
        提供注册界面
        :param request: 请求对象
        :return: 注册界面
        """
        return render(request, 'register.html')

    def post(self,request):
        #1.接收数据
        mobile=request.POST.get('mobile')
        password=request.POST.get('password')
        password2=request.POST.get('password2')
        smscode=request.POST.get('sms_code')

        #2.验证数据
            #2.1 参数是否齐全
        if not all ([mobile,password,password2,smscode]):
            return HttpResponseBadRequest('缺少必要的参数')

            #2.2 手机号的格式
        if not re.match(r'^1[3-9]\d{9}$', mobile):
            return HttpResponseBadRequest('请输入正确的手机号码')
            #2.3 密码是否符合格式
        if not re.match(r'^[0-9A-Za-z]{8,20}$', password):
            return HttpResponseBadRequest('请输入8-20位的密码')
            #2.4 密码和确认密码一致
        if password != password2:
            return HttpResponseBadRequest('两次输入的密码不一致')
            #2.5 短信验证码是否和reids中的一致
        redis_conn = get_redis_connection('default')
        sms_code_server = redis_conn.get('sms:%s' % mobile)
        if sms_code_server is None:
            return HttpResponseBadRequest('短信验证码已过期')
        if smscode != sms_code_server.decode():
            return HttpResponseBadRequest('短信验证码错误')
        #3.保存注册信息
        try:
            user = User.objects.create_user(username=mobile, mobile=mobile, password=password)
        except DatabaseError as e:
            logger.error(e)
            return HttpResponseBadRequest('注册失败')


        from django.contrib.auth import login
        login(request,user)
        #4.返回响应式跳转到指定页面
        #
        #
        response=redirect(reverse('home:index'))
        # return HttpResponse('注册成功，重定向首页')

        #设置cookie信息，以方便首页中用户信息展示的判断和用户信息的展示
        response.set_cookie('is_login',True)
        response.set_cookie('username',user.username,max_age=7*24*3600)

        return response


from django.http import HttpResponseBadRequest,HttpResponse
from libs.captcha.captcha import captcha
from django_redis import get_redis_connection
class ImageCodeView(View):

    def get(self,request):
        #获取前端传递过来的参数
        uuid=request.GET.get('uuid')
        #判断参数是否为None
        if uuid is None:
            return HttpResponseBadRequest('请求参数错误')
        # 获取验证码内容和验证码图片二进制数据
        text, image = captcha.generate_captcha()
        # 将图片验内容保存到redis中，并设置过期时间
        redis_conn = get_redis_connection('default')
        redis_conn.setex('img:%s' % uuid, 300, text)
        # 返回响应，将生成的图片以content_type为image/jpeg的形式返回给请求
        return HttpResponse(image, content_type='image/jpeg')


from django.http import JsonResponse
from utils.response_code import RETCODE
from random import randint
from libs.yuntongxun.sms import CCP
import logging
logger=logging.getLogger('django')
class SmsCodeView(View):

    def get(self,request):
        # 接收参数
        image_code = request.GET.get('image_code')
        uuid = request.GET.get('uuid')
        mobile=request.GET.get('mobile')

        # 校验参数
        if not all([image_code, uuid,mobile]):
            return JsonResponse({'code': RETCODE.NECESSARYPARAMERR, 'errmsg': '缺少必传参数'})

        # 创建连接到redis的对象
        redis_conn = get_redis_connection('default')
        # 提取图形验证码
        image_code_server = redis_conn.get('img:%s' % uuid)
        if image_code_server is None:
            # 图形验证码过期或者不存在
            return JsonResponse({'code': RETCODE.IMAGECODEERR, 'errmsg': '图形验证码失效'})
        # 删除图形验证码，避免恶意测试图形验证码
        try:
            redis_conn.delete('img:%s' % uuid)
        except Exception as e:
            logger.error(e)
        # 对比图形验证码
        image_code_server = image_code_server.decode()  # bytes转字符串
        if image_code.lower() != image_code_server.lower():  # 转小写后比较
            return JsonResponse({'code': RETCODE.IMAGECODEERR, 'errmsg': '输入图形验证码有误'})

        # 生成短信验证码：生成6位数验证码
        sms_code = '%06d' % randint(0, 999999)
        #将验证码输出在控制台，以方便调试
        logger.info(sms_code)
        # 保存短信验证码到redis中，并设置有效期
        redis_conn.setex('sms:%s' % mobile, 300, sms_code)
        # 发送短信验证码
        CCP().send_template_sms(mobile, [sms_code, 5],1)

        # 响应结果
        return JsonResponse({'code': RETCODE.OK, 'errmsg': '发送短信成功'})


class LoginView(View):

    def get(self,request):

        return render(request,'login.html')
    def post(self,request):
        # 1.接收参数
        mobile=request.POST.get('mobile')
        password = request.POST.get('password')
        remember=request.POST.get('remember')
        # 2.参数的验证
        #     2.1 验证手机号
        if not re.match(r'^1[3-9]\d{9}$', mobile):
            return HttpResponseBadRequest('请输入正确的手机号')
        #     2.2 验证密码是否符合规则
        if not re.match(r'^[0-9A-Za-z]{8,20}$', password):
            return HttpResponseBadRequest('密码不符合规则')
        # 3.用户认证登录
        # 使用系统自带的认证方法
        # 如果用户名和密码正确 返回user
        # 如果不正确 返回NONE
        from django.contrib.auth import authenticate
        # 默认的认证方法是对用户名的字段进行验证，所以我们要修改一下认证字段
        user = authenticate(mobile=mobile,password=password)
        if user is None:
            return HttpResponseBadRequest('用户名或密码错误')
        # 4.状态的保持
        from django.contrib.auth import login
        login(request, user)
        # 5.根据用户选择的是否记住登录状态来进行判断

        # 根据next参数进行跳转
        next_page=request.GET.get('next')
        if next_page:
            response = redirect(next_page)
        else:
            response = redirect(reverse('home:index'))
        if remember != 'on':
            # 没有记住用户：浏览器会话结束就过期
            request.session.set_expiry(0)
            # 设置cookie
            response.set_cookie('is_login', True)
            response.set_cookie('username', user.username, max_age=14 * 24 * 3600)
        else:
            # 记住用户：None表示两周后过期
            request.session.set_expiry(None)
            response.set_cookie('is_login', True, max_age=14 * 24 * 3600)
            response.set_cookie('username', user.username, max_age=30 * 24 * 3600)
        # 6.为了首页我们需要设置一些cookie
        # 7.返回响应
        return response


from django.contrib.auth import logout

class LogoutView(View):

    def get(self,request):
        # 清理session
        logout(request)
        # 退出登录，重定向到登录页
        response = redirect(reverse('home:index'))
        # 退出登录时清除cookie中的登录状态
        response.delete_cookie('is_login')

        return response

class ForgetPasswordView(View):

    def get(self,request):

        return render(request,'forget_password.html')

    def post(self,request):

        # 1.接受数据
        mobile=request.POST.get('mobile')
        password=request.POST.get('password')
        password2=request.POST.get('password2')
        smscode=request.POST.get('sms_code')

        # 2.验证数据
        #     2.1判断参数是否齐全
        if not all([mobile, password, password2, smscode]):
            return HttpResponseBadRequest('缺少必传参数')
        #     2.2判断手机号是否符合规则
        if not re.match(r'^1[3-9]\d{9}$', mobile):
            return HttpResponseBadRequest('请输入正确的手机号码')
        #     2.3判断密码是否符合规则
        if not re.match(r'^[0-9A-Za-z]{8,20}$', password):
            return HttpResponseBadRequest('请输入8-20位的密码')
        #     2.4判断确认密码和密码是否一致
        if password != password2:
            return HttpResponseBadRequest('两次输入的密码不一致')
        #     2.5判断短信验证码是否一致
        redis_conn = get_redis_connection('default')
        sms_code_server = redis_conn.get('sms:%s' % mobile)
        if sms_code_server is None:
            return HttpResponseBadRequest('短信验证码已过期')
        if smscode != sms_code_server.decode():
            return HttpResponseBadRequest('短信验证码错误')
        # 3.根据手机号进行数据查询
        try:
            user = User.objects.get(mobile=mobile)
        except User.DoesNotExist:
            # 如果该手机号不存在，则注册个新用户
            try:
                User.objects.create_user(username=mobile, mobile=mobile, password=password)
            except Exception:
                return HttpResponseBadRequest('修改失败，请稍后再试')
        else:
            # 修改用户密码
            user.set_password(password)
            user.save()
        # 6.进行页面跳转，跳转到登录界面
        response = redirect(reverse('users:login'))

        return response
        # 7.返回响应

from django.contrib.auth.mixins import LoginRequiredMixin

class UserCenterView(LoginRequiredMixin,View):

    def get(self,request):
        # 获得登录用户的信息
        user=request.user
        # 组织获取用户的信息
        context ={
            'username':user.username,
            'mobile':user.mobile,
            'avater':user.avatar.url if user.avatar else None,
            'user_desc':user.user_desc,
        }
        return render(request,'center.html',context=context)

    def post(self,request):
        # 接收数据
        user = request.user
        avatar = request.FILES.get('avatar')
        username = request.POST.get('username',user.username)
        user_desc = request.POST.get('desc',user.user_desc)

        # 修改数据库数据
        try:
            user.username=username
            user.user_desc=user_desc
            if avatar:
                user.avatar=avatar
            user.save()
        except Exception as e:
            logger.error(e)
            return HttpResponseBadRequest('更新失败，请稍后再试')

        # 返回响应，刷新页面
        response = redirect(reverse('users:center'))
        #更新cookie信息
        response.set_cookie('username',user.username,max_age=14*24*3600)
        return response

from home.models import ArticleCategory,Article
class WriteBlogView(LoginRequiredMixin,View):

    def get(self,request):
        # 获取博客分类信息
        categories = ArticleCategory.objects.all()

        context = {
            'categories': categories
        }
        return render(request, 'write_blog.html', context=context)

    def post(self,request):
        # 接收数据
        avatar = request.FILES.get('avatar')
        title = request.POST.get('title')
        category_id = request.POST.get('category')
        tags = request.POST.get('tags')
        sumary = request.POST.get('sumary')
        content = request.POST.get('content')
        user = request.user

        # 验证数据是否齐全
        if not all([avatar, title, category_id, sumary, content]):
            return HttpResponseBadRequest('参数不全')

        # 判断文章分类id数据是否正确
        try:
            article_category = ArticleCategory.objects.get(id=category_id)
        except ArticleCategory.DoesNotExist:
            return HttpResponseBadRequest('没有此分类信息')

        # 保存到数据库
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

        # 返回响应，跳转到文章详情页面
        # 暂时先跳转到首页
        return redirect(reverse('home:index'))