from django.contrib import admin
from django.urls import path, include
from . import views

# 正在部署的应用的名称
app_name = 'Nano'

urlpatterns = [
    path('', views.index, name='nano_index'),
    path('about/', views.about, name='nano_about'),
    path('project/', views.project, name='nano_project'),

    # mobileNet OD
    path('object-detection/', views.object_detection, name='object_detection'),
    path('main_interface/', views.main_interface, name='main_interface'),

    # yolov5s
    path('yolov5s/', views.yolov5s, name='yolov5s'),
    path('yolov5sOD/', views.yolov5sOD, name='yolov5sOD'),

    # 接收告警信息
    path('alert/', views.alert_data, name='alert_data'),

    # 输电线缺陷检测
    path('anomaly-detection/', views.anomaly_detection, name='anomaly_detection'),
]
