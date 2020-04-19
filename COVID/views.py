from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.

def index(request):
    html = '<h1 style = "color:red" > Hello World ! jcx</h1>'
    return HttpResponse(html)

def country(request,name):
    return HttpResponse('国家是{0}'.format(name))