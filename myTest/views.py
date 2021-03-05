import shutil

from django.shortcuts import render
from django.http import HttpResponse
import os
import zipfile
import shapefile



def index(request):


    return render(request, 'myTest/index.html')



