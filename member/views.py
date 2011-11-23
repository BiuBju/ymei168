#coding=utf-8

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf
import re

from ymei168.commonmt import *
from ymei168.member.models import *


def login(request):
    return HttpResponse("Login")

#验证用户注册表单
def checkregform(username,password,password2,uemail):
    if(not username):
        return 1,'用户名不能为空'
    if(not password):
        return 2,'密码不能为空'
    if(not password2):
        return 3,'确认密码不能为空'
    if(not uemail):
        return 4,'邮件不能为空'

    userlen=len(username)
    if(userlen>=4 and userlen<=20):
        tmparr=re.findall('\w',username)
        if(len(tmparr)!=userlen):
            return 1,'用户名只能为数字或字母'
    else:
        return 1,'用户长度为4-16'

    pwdlen=len(password)
    if(pwdlen>=4 and pwdlen<=16):
        tmparr=re.findall('\w',password)
        if(len(tmparr)!=pwdlen):
            return 2,'密码只能为数字或字母'
    else:
        return 2,'密码长度为4-16'
    if(password!=password2):
        return 3,'两个密码不匹配'

    match=re.search('\w+@(\w+.)+[a-z]{2,3}',uemail)
    if(not match):
        return 4,'邮件格式不对'

    if(duserisexist(username)==1):
        return 1,'用户名被占用'
    if(demailisexist(uemail)==1):
        return 10,'邮箱被占用'

    return 0, '注册成功！'

#用户注册
def register(request):
    if request.method == 'GET': #注册页面
        data = {}
        data.update(csrf(request))
        return render_to_response("member/register.html", data)
    elif request.method == 'POST': #处理注册表单
        username=gisempty(request.POST.get('username', None)) #用户名
        password=gisempty(request.POST.get('password', None)) #密码
        password2=gisempty(request.POST.get('password2', None)) #确认密码
        email=gisempty(request.POST.get('email', None)) #邮箱
        ip=request.META.get('REMOTE_ADDR', '0.0.0.0')
        
        status,result=checkregform(username,password,password2,email)
        
        if(status != 0):
            return HttpResponse(str(status)+":"+result)
        
        dinsertuser(username,password,email,ip) #插入数据库
        return HttpResponse("注册成功");


