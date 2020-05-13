from django.shortcuts import render
from django.http import HttpResponse
import os
import zipfile
import shapefile
from PIL import Image, ImageDraw
#解压文件
import rarfile

from .shaded_relief import shaded_relief
from .dem2img import dem2img

def index(request):
    global path
    if request.method == 'POST':
        flow = int(request.POST.get('flow'))
        if flow == 1:
            f = request.FILES.get('file_obj')
            path = os.path.join(os.path.dirname(os.getcwd()) + "/webGIS/data/shaded_relief/")
            with open(os.path.join(path+f.name), "wb") as file:
                for chunk in f.chunks():
                    file.write(chunk)
            return HttpResponse()
        elif flow == 2:
            f = request.FILES.get('file_obj')
            azimuth = int(request.POST.get('azimuth'))
            altitude = int(request.POST.get('altitude'))
            z = int(request.POST.get('z'))
            scale = int(request.POST.get('scale'))
            i = f.name
            shaded = shaded_relief()
            imgPath = shaded.drawing(path, i, azimuth, altitude, z,scale)
            # with open(os.path.join(img_path), 'wb+') as f:  # 图片上传
            #     for item in fafafa.chunks():
            #         f.write(item)
            return HttpResponse(imgPath)

    return render(request, 'shaded_relief/shaded_relief.html')

# Create your views here.
