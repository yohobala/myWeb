from django.urls import path

from . import views

app_name = 'polls' #命名空间
#这是这个app的链接
urlpatterns = [
    path('', views.index, name='index'),
    #实例 /polls/5/  5为问题的id号
    path('<int:question_id>/',views.detail,name='detail'),
    #实例 /polls/5/results/
    path('<int:question_id>/results/', views.results,name='results'),
    #实例 /polls/5/vote/
    path('<int:question_id>/vote/',views.vote,name='vote'),
]