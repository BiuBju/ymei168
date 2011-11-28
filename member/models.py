#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from datetime import *

from ymei168.commondb import *
from ymei168.commonmt import *


#检测用户名是否已被注册
def duserisexist(username):
    sql="SELECT name FROM ym_member WHERE name='%s'"%(g_sql_escape_string(username))
    data=g_sql_get_data(sql)
    if(not data):
        return 0  #未被注册
    else:
        return 1  #已注册

#检查邮箱是否被注册
def demailisexist(email):
    sql="select email from ym_member where email='%s'"%(g_sql_escape_string(email))
    data=g_sql_get_data(sql)
    if(not data):
        return 0  # 未被占用
    else:
        return 1  # 己被使用

#用户注册
def dinsertuser(username,password,email,ip):
    regdate=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    lastlogin=regdate
    logintimes=1
    
    sql="INSERT INTO ym_member SET name='%s',password='%s',email='%s',login_times=%d,last_login='%s',reg_date='%s',ip='%s'"%(
        g_sql_escape_string(username),g_sql_escape_string(password),g_sql_escape_string(email),
        logintimes,g_sql_escape_string(lastlogin),g_sql_escape_string(regdate),ip
    )

    gprint(sql)

    g_sql_set_data(sql) #插入数据库

#用户登陆
def dcheckuser(username,password):
    sql="select * from ym_member where name='%s'"%(g_sql_escape_string(username))
    gprint(sql)
    data=g_sql_get_one_data(sql)
    if(not data):
        return 1,'用户名不存在'
    else:
        realpwd=data['password']
    if(realpwd==password):
        today=datetime.now().strftime('%Y-%m-%d')
        data['login_times']=data['login_times']+1
        data['last_login']=today
        # 更新用户信息
        dloginupdate(data['login_times'],data['last_login'],data['member_id'])
        return 0,data #返回用户信息
    else:
        return 2,'密码错误'
        

def dloginupdate(logintimes,lastlogin,memberid):
    '''
    更新用户登录次数和最后一次登陆的时间
    @author magicalboy
    @date 2011.11.26
    '''
    sql="update ym_member set login_times='%s',last_login='%s' where \
    member_id=%d"%(
        g_sql_escape_string(logintimes),
        g_sql_escape_string(lastlogin),
        memberid
    )
    
    g_sql_set_data(sql)


def dupdateuser(nickname,realname,gender,province,city,county,address,phone,memberid):
    '''
    更新用户信息：nickname,realname,gender,province,city,county,address,phone
    @author magicalboy
    @date 11.11.26
    '''
    sql="UPDATE ym_member SET nickname='%s',realname='%s',gender='%s',province=%d,\
    city=%d,county=%d,address='%s',phone='%s' WHERE member_id=%d"%(
        g_sql_escape_string(nickname),g_sql_escape_string(realname),
        gender,int(province),int(city),int(county),g_sql_escape_string(address),
        g_sql_escape_string(phone),int(memberid)
    )
    
    gprint(sql)
    g_sql_set_data(sql)
    
    
    