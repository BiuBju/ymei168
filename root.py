#coding=utf-8
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db import *
from django.db.backends import *
import string
from django.views.decorators.cache import cache_page
from time import time, localtime, strftime


def index(request):
    return HttpResponse("index")

def testdatabase(request):
    sql="select * from ym_member;"
    cursor=connection.cursor()
    states=cursor.execute(sql)
    return HttpResponse(states);
