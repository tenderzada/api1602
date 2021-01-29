from django.http import JsonResponse
from django.shortcuts import render
# 导入 HttpResponse 模块
from django.http import HttpResponse
from .models import NewsPost
import markdown
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    # return HttpResponse("hello world!")
    # context = {}
    # return render(request, 'nano/index.html', context)

    # 取出所有新闻
    news = NewsPost.objects.all()
    # print(news)
    # 每页显示3篇新闻
    paginator = Paginator(news,3)

    news_1 = paginator.get_page(1)
    # 需要传递给模板（templates）的对象
    context = { 'news': news_1 }
    # render函数：载入模板，并返回context对象
    return render(request, 'nano/index.html', context)

def new_detail(request, id):
    new = NewsPost.objects.get(id=id)

    # 将markdown语法渲染成html格式
    new.body = markdown.markdown(new.body,
        extensions=[
            # 包含 缩写、表格等常用扩展
            'markdown.extensions.extra',
            # 语法高亮扩展
            'markdown.extensions.codehilite',
        ])
    context = {'new':new}
    return render(request,'nano/detail.html',context)