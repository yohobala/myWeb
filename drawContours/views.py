from django.shortcuts import render
from django.http import HttpResponse
import os
import zipfile
import shapefile
from PIL import Image, ImageDraw
#解压文件
import rarfile

from .contour import contour
from .drawContours import drawContours

def index(request):
    if request.method == 'POST':
        flow = int(request.POST.get('flow'))
        if flow == 1:
            f = request.FILES.get('file_obj')
            path = os.path.join(os.path.dirname(os.getcwd()) + "/webGIS/data/drawContours/")
            interval =  int(request.POST.get('interval'))
            height = int(request.POST.get('height'))
            iwidth = int(request.POST.get('iwidth'))
            iheight = int(request.POST.get('iheight'))
            color = request.POST.get('color')
            with open(os.path.join(path+f.name.split('.')[0]+'.asc'), "wb") as file:
                for chunk in f.chunks():
                    file.write(chunk)
            contour().contour(path,f.name,interval,height)
            data = drawContours().drawContours(path,f.name,iwidth,iheight,color)
            return HttpResponse(data)
        elif flow == 2:
            f = request.FILES.get('file_obj')
            path = os.path.join(os.path.dirname(os.getcwd()) + "/webGIS/data/drawContours/")
            filename = f.name
            filePath = path + filename.split('.')[0] + '/'

            iwidth = int(request.POST.get('iwidth'))
            iheight = int(request.POST.get('iheight'))
            color = request.POST.get('color')

            with open(os.path.join(path+filename), 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)

            zip_file = zipfile.ZipFile(path+filename)
            zip_list = zip_file.namelist()  # 得到压缩包里所有文件

            path = filePath

            for file in zip_list:
                zip_file.extract(file, path)  # 循环解压文件到指定目录

            l = os.listdir(path)
            existFile = 0 ;
            for file in l:
                if file[-3:] == 'shp':
                    data = drawContours().drawContours(path, file, iwidth, iheight, color)
                    existFile = 1 ;

            if existFile !=1 :
                path = path + filename.split('.')[0] + '/'
                l = os.listdir(path)
                for file in l:
                   if file.split('.')[1] == 'shp':
                       data = drawContours().drawContours(path, file, iwidth, iheight, color)
            # with open(os.path.join(img_path), 'wb+') as f:  # 图片上传
            #     for item in fafafa.chunks():
            #         f.write(item)
            return HttpResponse(data)

    return render(request, 'drawContours/drawContours.html')
