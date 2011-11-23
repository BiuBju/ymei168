#coding=utf-8

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
    
    sql="INSERT INTO ym_member SET name='%s',password='%s',email='%s',reg_date='%s',ip='%s'"%(
        g_sql_escape_string(username),g_sql_escape_string(password),
        g_sql_escape_string(email),g_sql_escape_string(regdate),ip
    )

    gprint(sql)

    g_sql_set_data(sql) #插入数据库

