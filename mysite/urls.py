"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import  url
from django.conf import settings
from django.conf.urls.static import static
#总链接，为了连接到每个app,如果不设置，urls里面就找不到，比如不设置COVID
#就不能打开127.0.0.1:8000/COVID
urlpatterns = [
    path('',include('homepage.urls')),
    path('dotDensity/',include('dot_density.urls')),
    path('COVID/',include('COVID.urls')),
    path('admin/', admin.site.urls),
    path('isogram/',include('isogram.urls')),
    path('shadedrelief/',include('shaded_relief.urls')),
    path('drawContours/',include('drawContours.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
