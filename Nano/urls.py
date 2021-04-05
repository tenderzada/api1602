# in pollsapi/urls.py
from django.contrib import admin
from django.urls import path, include
from . import views

# 正在部署的应用的名称
app_name = 'Nano'

urlpatterns = [
    path('', views.index, name='nano_index'),
    path('about/', views.about, name='nano_about'),
    path('project/', views.project, name='nano_project'),
    path('object-detection/', views.object_detection, name='object_detection'),
    path('new-detail/<int:id>/',views.new_detail,name='new_detail'),
    path('main_interface/', views.main_interface, name='main_interface'),
]
