from django.conf.urls import url
from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
# namespace
app_name = '等值图'

urlpatterns = [

#上传文件
path('', views.index, name='文件上传'),

#显示结果
path('Result/',views.Result, name='结果'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
