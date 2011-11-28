#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
import re

from ymei168.commonmt import *
from ymei168.member.models import *
from ymei168.region.models import *


def index(request):
    '''
    用户首页
    magicalboy 11.11.24
    '''
    if(giflogin(request)):
        province_list = dgetallprovinces(1) #获取中国所有省
        city_list = dgetcitybyprovince(request.session.get('province')) # 获取用户所在省的城市
        county_list = dgetcountybycity(request.session.get('city')) # 获取用户所在市的县/区
        return render_to_response(
            "member/index.html",
            {'province_list':province_list,'city_list':city_list,'county_list':county_list},
            context_instance=RequestContext(request)
        )
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
    request.session['nickname'] = data['nickname']
    request.session['realname'] = data['realname']
    request.session['email'] = data['email']
    request.session['gender'] = data['gender']
    request.session['province'] = data['province']
    request.session['city'] = data['city']
    request.session['county'] = data['county']
    request.session['address'] = data['address']
    request.session['phone'] = data['phone']
    

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
        

def logout(request):
    '''
    退出登陆
    magicalboy 11.11.24
    '''
    request.session.flush()

    return HttpResponseRedirect("/member/login/")
    

#@csrf_exempt
def queryarea(request):
    '''
    查询城市和地区
    @author magicalboy
    @since 11.11.26
    '''
    
    if request.method == 'POST':
        from django.utils import simplejson
        action = gisempty(request.POST.get('action', None))
        regionid=gisempty(request.POST.get('region_id', None))
        
        if action == "getcity":
            #获取城市和地区
            if regionid:
                city_list = dgetcitybyprovince(int(regionid)) # 获取 regionid 省的城市
                county_list = dgetcountybycity(city_list[0]['region_id']) # 获取 regionid 省的第一个城市的县/区
                data = {'city_list':city_list, 'county_list':county_list}
                return HttpResponse(simplejson.dumps(data),mimetype="application/json")

        elif action == "getcounty":
            #获取地区
            if regionid:
                county_list = dgetcountybycity(int(regionid)) # 获取regionid城市的县/区
                data = {'county_list':county_list}
                return HttpResponse(simplejson.dumps(data),mimetype="application/json")


def membermanager(request):
    '''
    用户管理
    @author magicalboy
    @since 11.11.26
    '''
    
    if giflogin(request) and request.method == 'POST':
        action = gisempty(request.POST.get('action', None))
        memberid = request.session.get('uid')

        if action == 'update': #用户修改
            nickname=gisempty(request.POST.get('nickname', None))
            realname=gisempty(request.POST.get('realname', None))
            gender=gisempty(request.POST.get('gender', None))
            province=gisempty(request.POST.get('province', None))
            city=gisempty(request.POST.get('city', None))
            county=gisempty(request.POST.get('county', None))
            address=gisempty(request.POST.get('address', None))
            phone=gisempty(request.POST.get('phone', None))
            status,result=checkupdateform(request,nickname,realname,gender,province,city,county,address,phone)

            if(status != 0):
                return HttpResponse(str(status)+":"+result)
            else:
                dupdateuser(nickname,realname,gender,province,city,county,address,phone,memberid) #更新用户信息
                updatesession(request,nickname,realname,gender,province,city,county,address,phone) #更新 session
                return HttpResponseRedirect("/member/")
        else:
            return HttpResponseRedirect("/member/")
    else:
        return logout(request)


def checkupdateform(request,nickname,realname,gender,province,city,county,address,phone):
    '''
    验证用户修改表单
    @author magicalboy
    @since 11.11.26
    '''
    if(not nickname):
        return 1,'用户名昵称不能为空'
    if(not realname):
        return 2,'用户真实姓名不能为空'
    if(not gender):
        return 3,'用户性别不能为空'
    if(not province or not city or not county):
        return 4,'用户所在地信息不完整'
    if(not address):
        return 5,'用户详细地址不能为空'
    if(not phone):
        return 6,'联系电话不能为空'

    nicklen=len(nickname)
    if(nicklen<4 and nicklen>=20):
        return 1,'用户昵称长度为4-16'

    reallen=len(realname)
    if(reallen<4 and reallen>16):
        return 2,'用户真实姓名长度错误'

    return 0, '更新成功！'


def updatesession(request,nickname,realname,gender,province,city,county,address,phone):
    '''
    用户更新成功后更新 session
    @author magicalboy
    @date 11.11.26
    '''
    request.session['nickname']=nickname
    request.session['realname']=realname
    request.session['gender']=gender
    request.session['province']=int(province)
    request.session['city']=int(city)
    request.session['county']=int(county)
    request.session['address']=address
    request.session['phone']=phone
    