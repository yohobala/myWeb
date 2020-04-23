from django.shortcuts import render
from .forms import UploadFileForm
from django.http import HttpResponse
import os
import zipfile

#解压文件
import rarfile

from .We import We

def index(request):
  return render(request, 'isogram/getFile.html')

def Result(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        f = request.FILES['file']
        path1 = os.path.join(os.path.dirname(os.getcwd())+"/webGIS/data/",f.name)
        path2 = os.path.dirname(os.getcwd())+"/webGIS/data/"
        with open(os.path.join(path1), 'wb+') as destination:
                  for chunk in f.chunks():
                       destination.write(chunk)

        zip_file = zipfile.ZipFile(path1)
        zip_list = zip_file.namelist()  # 得到压缩包里所有文件

        for f in zip_list:
            zip_file.extract(f, path2)  # 循环解压文件到指定目录
        path = path1.split('.')[0] + '/'
        l = os.listdir(path)

        for i in l:
            if i.split('.')[1] == 'shp':
                we = We()
                imgPath = We.gg(path,i)
    else:
        form = UploadFileForm()
    return render(request, 'isogram/Result.html',{'image':imgPath})
