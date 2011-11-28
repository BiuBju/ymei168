#coding=utf-8

from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',
    (r'^$', 'ymei168.member.views.index'), #用户首页
    (r'^register/$', 'ymei168.member.views.register'), # 用户注册
    (r'^login/$','ymei168.member.views.login'), # 用户登陆
    (r'^logout/$','ymei168.member.views.logout'), #用户退出登陆
    (r'^action/$','ymei168.member.views.membermanager'), #用户管理
    (r'^captcha/', 'ymei168.member.views.captcha'), #验证码
    (r'^queryarea/$', 'ymei168.member.views.queryarea'), #查询地区
) 
