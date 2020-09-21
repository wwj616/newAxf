from django.conf.urls import url

from UserApp import views

urlpatterns = [
    url(r'^toRegister/',views.toRegister),
    url(r'^toLogin/',views.toLogin,name='toLogin'),
#    验证码
    url(r'^get_code/',views.get_code),

#     用户名字的后台验证
    url(r'^checkName/',views.checkName),

#     发送邮件
#     url(r'^sendEmail/',views.sendEmail),

#     注册
    url(r'^register/',views.register,name='register'),

#     激活
    url(r'^account/',views.account),

#     登陆
    url(r'^login/',views.login,name='login'),

#     退出
    url(r'^logout/',views.logout,name='logout'),
]