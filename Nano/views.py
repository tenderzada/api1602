from django.http import JsonResponse
from django.shortcuts import render
# 导入 HttpResponse 模块
from django.http import HttpResponse
from .models import NewsPost
import markdown
from django.core.paginator import Paginator
# Create your views here.

#od
from PIL import Image
import numpy as np
import base64
import io
import os
import json
from .tf_inference import load_model, inference
os.environ['CUDA_VISIBLE_DEVICES'] = '0'

sess, detection_graph = load_model()

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

def object_detection(request):
    return render(request, 'nano/object_detection.html')

def main_interface(request):
    if request.method == 'POST':
        print("yes")
        # response = request.POST.get('image')
        response = json.loads(request.body)
        # print(response)
        # response = request.get_json()
        data_str = response['image']
        point = data_str.find(',')
        base64_str = data_str[point:]  # remove unused part like this: "data:image/jpeg;base64,"

        image = base64.b64decode(base64_str)       
        img = Image.open(io.BytesIO(image))

        if(img.mode!='RGB'):
            img = img.convert("RGB")
        
        # convert to numpy array.
        img_arr = np.array(img)

        # do object detection in inference function.
        results = inference(sess, detection_graph, img_arr, conf_thresh=0.5)
        print(results)
        print(type(results))
        return HttpResponse(json.dumps(results))
        # return JsonResponse(results)
    else:
        print("error")

def about(request):
    return render(request, 'nano/about.html')

def project(request):
    return render(request, 'nano/portfolio-1-col.html')