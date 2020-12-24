from django.http import JsonResponse
from django.shortcuts import render
# 导入 HttpResponse 模块
from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse("hello world!")
    context = {}
    return render(request, 'nano/index.html', context)