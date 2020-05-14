from django.shortcuts import render
from django.http import HttpResponse
import os
import zipfile
import shapefile
from PIL import Image, ImageDraw
#解压文件
import rarfile

from .showLidar import showLidar

def index(request):
    global path
    if request.method == 'POST':
        f = request.FILES.get('file_obj')
        width = int(request.POST.get('width'))
        height = int(request.POST.get('height'))
        color = request.POST.get('color')
        print(f.name)

        filename = f.name.split('.')[0]

        path1 = os.path.join(os.path.dirname(os.getcwd()) + "/webGIS/data/showLidar/")
        filePath = path1 + filename + '.zip'
        with open(os.path.join(filePath), 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

        zip_file = zipfile.ZipFile(filePath)
        zip_list = zip_file.namelist()  # 得到压缩包里所有文件

        path = path1 + filename + '/'

        for file in zip_list:
            zip_file.extract(file, path)  # 循环解压文件到指定目录

        l = os.listdir(path)
        existFile = 0
        for file in l:
            if file[-3:] == 'las':
                img= showLidar()
                imgPath = img.showLidar(path, file)
                existFile = 1
        if existFile != 1:
            path = path + filename + '/'
            l = os.listdir(path)
            for file in l:
                if file.split('.')[1] == 'las':
                    img = showLidar()
                    imgPath = img.showShp(path, file, width, height, color)

        return HttpResponse(imgPath)


    return render(request, 'showLidar/showLidar.html')