#coding=utf-8

from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',
    (r'^register/$', 'ymei168.member.views.register'), # 用户注册
    (r'^login/$','ymei168.member.views.login'), # 用户登陆
) 
