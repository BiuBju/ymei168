#coding=utf-8

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf
import re

from ymei168.commonmt import *
from ymei168.member.models import *

def index(request):
    '''
    用户首页
    magicalboy 11.11.24
    '''
    if(giflogin(request)):
        return render_to_response("member/index.html",{},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect("/member/login/"); #重定向到登陆页面


def login(request):
    '''
    用户登陆
    magicalboy 11.11.23
    '''
    if request.method == 'GET': #登陆页面
        data = {}
        data.update(csrf(request))
        return render_to_response("member/login.html", data)
    if request.method == 'POST': #登陆处理
        username=gisempty(request.POST.get('username', None)) #用户名
        password=gisempty(request.POST.get('password', None)) #密码
        
        status,result=checkloginform(request,username,password)

        if(status != 0):
            return HttpResponse(str(status)+":"+result)
        else:
            setsession(request,result) #设置session
            return HttpResponseRedirect("/member/")


def checkloginform(request,username,password):
    '''
    验证用户登陆表单
    magicalboy 11.11.23
    '''
    if(not username):
        return 1,'用户名不能为空'
    if(not password):
        return 2,'密码不能为空'

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

    return dcheckuser(username,password) #检测用户


def setsession(request,data):
    '''
    设置session
    magicalboy 11.11.24
    '''
    request.session['username'] = data['name']
    request.session['uid'] = data['member_id']


def checkregform(request,username,password,password2,uemail,verifycode):
    '''
    验证用户注册表单
    magicalboy 11.11.22
    '''
    if(not username):
        return 1,'用户名不能为空'
    if(not password):
        return 2,'密码不能为空'
    if(not password2):
        return 3,'确认密码不能为空'
    if(not uemail):
        return 4,'邮件不能为空'
    if(not verifycode):
        return 5,'验证码不能为空'

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
        
    if(request.session.get('captcha')!=verifycode):
        return 5,'验证码不正确'

    if(duserisexist(username)==1):
        return 1,'用户名被占用'
    if(demailisexist(uemail)==1):
        return 4,'邮箱被占用'

    return 0, '注册成功！'


def register(request):
    '''
    用户注册
    magicalboy 11.11.22
    '''
    if request.method == 'GET': #注册页面
        data = {}
        data.update(csrf(request))
        return render_to_response("member/register.html", data)
    elif request.method == 'POST': #处理注册表单
        username=gisempty(request.POST.get('username', None)) #用户名
        password=gisempty(request.POST.get('password', None)) #密码
        password2=gisempty(request.POST.get('password2', None)) #确认密码
        email=gisempty(request.POST.get('email', None)) #邮箱
        verifycode=gisempty(request.POST.get('captcha', None)) #验证码
        ip=request.META.get('REMOTE_ADDR', '0.0.0.0')

        status,result=checkregform(request,username,password,password2,email,verifycode)

        if(status != 0):
            return HttpResponse(str(status)+":"+result)
        
        dinsertuser(username,password,email,ip) #插入数据库
        
        return HttpResponseRedirect("/member/login/"); #重定向到登陆页面


def captcha(request):
    '''
    验证码
    magicalboy 11.11.23
    '''
    return verifycode(request)
        

def logout (request):
    '''
    退出登陆
    magicalboy 11.11.24
    '''
    try:
        del request.session['username']
        del request.session['uid']
    except KeyError, e:
        pass
    return HttpResponseRedirect("/member/login/")