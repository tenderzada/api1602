# in pollsapi/urls.py
from django.contrib import admin
from django.urls import path, include
from . import views

# 正在部署的应用的名称
app_name = 'Nano'

urlpatterns = [
    path('index/', views.index, name='nano_index'),
    path('new-detail/<int:id>/',views.new_detail,name='new_detail'),
]
