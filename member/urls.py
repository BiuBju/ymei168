#conding=utf-8

from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',
    (r'^login/','ymei168.member.views.login'),

) 
