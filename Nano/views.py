from django.http import JsonResponse
from django.shortcuts import render
# 导入 HttpResponse 模块
from django.http import HttpResponse
from django.core.paginator import Paginator

#mobileNet od
from PIL import Image
import numpy as np
import base64
import io
import os
import json
from .tf_inference import load_model, inference
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
sess, detection_graph = load_model()

# alert
from .models import Alert
import re
from .forms import AlertForm

# yolov5s OD
import datetime
import shutil
from datetime import timedelta
from .AIDetector_pytorch import Detector
import core.main
import time
import cv2

# 访问首页
def index(request):
    # render函数：载入模板，并返回context对象
    return render(request, 'nano/index.html')

# 关于我们
def about(request):
    return render(request, 'nano/about.html')

# 查看项目
def project(request):
    return render(request, 'nano/portfolio-1-col.html')

# mobileNet OD
def object_detection(request):
    return render(request, 'nano/object_detection.html')

# mobileNet OD
def main_interface(request):
    if request.method == 'POST':
        print("yes")
        response = json.loads(request.body)
        data_str = response['image']
        print('data_str',type(data_str))
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
        # print(results)
        # print(type(results))
        return HttpResponse(json.dumps(results))
    else:
        print("error")

# yolov5s OD for 输电线缺陷检测
def yolov5s(request):
    return render(request, 'nano/yolov5s.html')

# yolov5s OD for 输电线缺陷检测
def yolov5sOD(request):
    if request.method == 'POST':
        print("yes")
        response = json.loads(request.body)
        data_str = response['image']
        print('data_str',type(data_str))
        point = data_str.find(',')
        base64_str = data_str[point:]  # remove unused part like this: "data:image/jpeg;base64,"

        image = base64.b64decode(base64_str)       
        img = Image.open(io.BytesIO(image))

        if(img.mode!='RGB'):
            img = img.convert("RGB")
        
        # convert to numpy array.
        img_arr = np.array(img)
        print(type(img_arr))

        now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
        print('now:',now)
        src_path = now + r'.jpg'
        print("src_path:",src_path)
        cv2.imwrite(src_path, img_arr)
        shutil.copy(src_path,'static\ct')
        image_path = os.path.join('static\ct',now+r'.jpg')
        yolov5s = Detector()
        pid, image_info, pred_boxes = core.main.c_main(
            image_path, yolov5s, 'jpg')
        # print('pid:',pid)
        # print('image_info:',image_info)
        # print('pred_bboxs:',pred_boxes)
        results = pred_boxes
        return HttpResponse(json.dumps(results))
    else:
        print("error")

# 输电线缺陷检测
def anomaly_detection(request):
    return render(request, 'nano/anomaly_detection.html')


# 接收告警消息，写入数据库
def alert_data(request):
    if request.method == 'POST':
        # 将提交的数据赋值到表单实例
        alert_form = AlertForm(data=request.POST)
        # 判断数据是否满足模型要求
        if alert_form.is_valid():
            # 保存数据，但是暂时不提交
            new_alert = alert_form.save(commit=False)
            new_alert.save()
            print("Receive Alert, please be careful !!!")
            # print(new_alert['anomaly_img'])
            return HttpResponse("POST success")
        else:
            return HttpResponse("POST error")
    else:
        return HttpResponse("please use post")
