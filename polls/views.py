from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Question
from  django.template import loader
# Create your views here.
#网页的内容,你的视图可以从数据库里读取记录，可以使用一个模板引擎（比如 Django 自带的，或者其他第三方的），
# 可以生成一个 PDF 文件，可以输出一个 XML，创建一个 ZIP 文件，你可以做任何你想做的事，使用任何你想用的 Python 库。
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)#载入模板，填充上下文，再返回由它生成的 HttpResponse 对象

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "你正在寻在{0}问题的答案"
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}

    return render(request, 'polls/index.html', context)

def vote(requset, question_id):
    return  HttpResponse("你正在给{0}问题投票".format(question_id))