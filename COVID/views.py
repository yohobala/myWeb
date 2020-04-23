import csv
import os

from django.shortcuts import render
from  .models import Country
from django.http import Http404, HttpResponse
from django.shortcuts import render,get_object_or_404
# Create your views here.

def index(request):
    return render(request,'COVID/homepage.html')

def country(request):
    Country_name = request.GET.get('q')
    print(Country_name)
    if Country_name == 'World' or Country_name == '全球':
        Country_name = 'World'
    else:
        try:
            list =  open(os.path.dirname(os.getcwd())+'/webGIS/crawler/country.csv', 'r')
            list_data = csv.reader(list)
            for line in list_data:
                if line[0] == Country_name:
                    Country_name = line[1]
                elif line[1] == Country_name:
                    Country_name = line[1]
                elif line[2] == Country_name:
                    Country_name = line[2]
            print(Country_name)
            # filter是返回列表，如果啥也没搜索到，返回空字符串，get是返回单个结果。0个或多个都会报错
            # country 返回一个QuerySet，QuerySet当是可迭代对象时，用values()返回一个列表嵌套字典形式[ {} ]
            # 用values_list()返回一个列表嵌套元组形式[ () ]
            # country = Country.objects.filter(english_name=Country_name)
            # name = Country_name
        except Country.DoesNotExist:
            raise Http404('没有这个国家/地区数据')
    # country_name = get_object_or_404(Country,name = Country_name)
    return render(request,'COVID/'+Country_name+'.html')#,{'country':country,'name':name}

