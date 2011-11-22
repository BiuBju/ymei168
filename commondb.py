#coding=utf-8

from django.db import models
from django.db import connection
from django.db.backends import util
from django.core.cache import cache
import MySQLdb;

#查询数据
def g_sql_get_data(sql):
    cursor = connection.cursor()
    cursor.execute(sql);
    data = util.dictfetchall(cursor)
    return data;

#查询一条数据
def g_sql_get_one_data(sql):
    data =  g_sql_get_data( sql )
    if(len(data)>=1):
       return data[0];
    return []

#判断是否存在记录
def g_sql_have_data(sql):
    data =  g_sql_get_data( sql )
    if(len(data)>=1):
       return True;
    else:
       return False;


#最后插入自动增长ID数值
def g_sql_last_id():
    data = g_sql_get_data("select LAST_INSERT_ID() 'count'");
    return data[0]['count'];
#插入数据
def g_sql_set_data(sql):
    cursor = connection.cursor()
    return cursor.execute(sql);
#查询条数
def g_sql_get_data_count(sql):
    cursor = connection.cursor()
    cursor.execute("select count(*) 'count' from "+sql)
    data = util.dictfetchall(cursor)
    if data:
        return  long(data[0]['count'])
    return 0

#查询条数及翻页页面数
def g_sql_get_data_pagecount(sql,pagecount):
    data = g_sql_get_data_count(sql);
    count = data%int(pagecount)
    if(count >0):
       count =1;
    count = count+data/pagecount;
    return data,count;

#查询翻页某页数据
def g_sql_get_data_pagelimit(sql,page,pagecount):
    page = int(page);
    pagecount = int(pagecount)
    index = (page-1) * pagecount
    if(index <0):
        index =0;
    sql = sql + " limit "+str(index)+", "+str(pagecount);

    return g_sql_get_data(sql);

#字符串转义 所有SQL里面的变量必须转义后加入sql语句中 整数类型的必须 int()
def g_sql_escape_string(sql):
    return MySQLdb.escape_string(str(sql))

#查询多条语句时候 需要将一个查询ID的数组转成  =“"某数值" 或者是 in ('数值1','数值2')
def g_sql_join_array(input):
     if(len(input)==0):
           return "";

     if(len(input)==1):
         return "= "+"'"+str(input[0])+"'"

     returndata=""
     for item in input:
        returndata  = returndata + "'"+str(item)+ "',";

     returndata = "in ("+returndata[0:len(returndata)-1]+")";
     return returndata;