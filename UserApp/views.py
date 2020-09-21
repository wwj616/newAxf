from io import BytesIO

from PIL import Image, ImageFont
from PIL.ImageDraw import ImageDraw
from django.contrib.auth.hashers import make_password, check_password
from django.core.cache import cache
from django.core.mail import send_mail

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader
from django.urls import reverse


from UserApp.views_helper import sendEmail

from UserApp.models import AxfUser
from axf import settings


def toRegister(request):
    return render(request,'axf/user/register/register.html')


def toLogin(request):
    return render(request,'axf/user/login/login.html')

def get_code(request):
    # 初始化画布，初始化画笔
    mode = "RGB"

    size = (100, 50)

    red = get_color()

    green = get_color()

    blue = get_color()

    color_bg = (red, green, blue)

    image = Image.new(mode=mode, size=size, color=color_bg)

    imagedraw = ImageDraw(image, mode=mode)

    imagefont = ImageFont.truetype(settings.FONT_PATH, 50)

    verify_code = generate_code()

    request.session['verify_code'] = verify_code

    for i in range(4):
        fill = (get_color(), get_color(), get_color())
        imagedraw.text(xy=(20*i, 0), text=verify_code[i], font=imagefont, fill=fill)

    for i in range(100):
        fill = (get_color(), get_color(), get_color())
        xy = (random.randrange(100), random.randrange(50))
        imagedraw.point(xy=xy, fill=fill)

    fp = BytesIO()

    image.save(fp, "png")

    return HttpResponse(fp.getvalue(), content_type="image/png")









import random


def get_color():
    return random.randrange(256)

def generate_code():
    source = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"
    code = ""
    for i in range(4):
        code += random.choice(source)
    return code


def checkName(request):
    data = {
        'status': 200,
    }

    name = request.GET.get('name')

    user = AxfUser.objects.filter(name=name)

    if user.count() > 0:
        data['msg'] = '用户名字已存在'
        data['status'] = 204
    else:
        data['msg'] = '用户名字可以使用'

    return JsonResponse(data=data)


# def sendEmail(request):
#
#     index = loader.get_template('axf/user/register/active.html')
#
#     context = {
#         'name':'action',
#         'url':'https://www.baidu.com'
#     }
#     index_value = index.render(context)
#
#
#     # subject, message, from_email, recipient_list,
#     # 主题       邮件内容   发送者      接收者
#     subject = '测试发送邮件'
#     message = index_value
#     from_email = 'yulin_ljing@163.com'
#     recipient_list = ['yulin_ljing@163.com']
#     send_mail(subject=subject,message='',html_message=message,from_email=from_email,recipient_list=recipient_list)
#
#     return HttpResponse('发送邮件成功')
import uuid

def register(request):

    name = request.POST.get('name')
    password = request.POST.get('password')

    password = make_password(password)

    email = request.POST.get('email')
    icon = request.FILES.get('icon')

    user = AxfUser()
    user.name = name
    user.password = password
    user.email = email
    user.icon = icon

    u_token = uuid.uuid4()

    user.token = u_token

    user.save()

    sendEmail(name,email,u_token)

    cache.set(u_token,user.id,timeout=60)

    return redirect(reverse('axfuser:toLogin'))


def account(request):

    token = request.GET.get('token')
    user_id = cache.get(token)

    if user_id:

        user= AxfUser.objects.get(pk=user_id)

        user.active = True

        user.save()
        # 激活次数设置为一次
        cache.delete(token)

        return HttpResponse('激活成功')
    else:
        return HttpResponse('邮件已过期，请重新发送邮件')


def login(request):

    icode = request.POST.get('icode')

    verify_code = request.session.get('verify_code')

    if icode.lower() == verify_code.lower():
        name = request.POST.get('name')
        users = AxfUser.objects.filter(name=name)
        if users.exists():
            user = users.first()
            password = request.POST.get('password')
            if check_password(password,user.password):
                if user.active == True:
                    request.session['user_id']=user.id
                    return redirect(reverse('axfmine:mine'))
                else:
                    context = {
                        'msg': '账号未激活'
                    }
                    return render(request, 'axf/user/login/login.html', context=context)

            else:
                context = {
                    'msg': '用户名字或者密码错误'
                }
                return render(request, 'axf/user/login/login.html', context=context)
        else:
            context = {
                'msg':'用户名字或者密码错误'
            }
            return render(request, 'axf/user/login/login.html', context=context)

    else:
        context = {
            'msg':'验证码不正确'
        }
        return render(request,'axf/user/login/login.html',context=context)


def logout(request):
    request.session.flush()
    return redirect(reverse('axfmine:mine'))