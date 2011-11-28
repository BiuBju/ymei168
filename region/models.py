#coding=utf-8

from django.db import models

from ymei168.commondb import *
from ymei168.commonmt import *


def dgetallprovinces(countryid):
    '''
    获取countryId的国家的所有省
    @author magicalboy
    @date 2011.11.26
    '''
    
    sql="SELECT region_id,region_name FROM ym_region WHERE parent_id='%d'"%countryid
    gprint(sql)
    data=g_sql_get_data(sql)
    
    return data
    
    
def dgetcitybyprovince(provinceid):
    '''
    获取provinceid省的所有城市
    @author magicalboy
    @date 2011.11.26
    '''

    return dgetallprovinces(provinceid)
    
    
def dgetcountybycity(cityid):
    '''
    获取cityid市的所有县/区
    @author magicalboy
    @date 2011.11.26
    '''

    return dgetallprovinces(cityid)