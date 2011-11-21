#conding=utf-8

from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',
   (r'^register', 'ymei168.member.views.register'),
   (r'^login/$','ymei168.member.views.login'),

) 
