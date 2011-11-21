#!/usr/bin/env python
#conding=utf-8
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
import string

def login(request):
    return HttpResponse("Login")

def register(request):
    return render_to_response("member/register.html")
