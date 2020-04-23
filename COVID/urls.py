from django.conf.urls import url
from  django.urls import path
from  . import  views #将当前目录下的views导入

#这是这个app的链接
urlpatterns = [
    path('', views.index),
    url(r'^search/$', views.country, name='search')
]