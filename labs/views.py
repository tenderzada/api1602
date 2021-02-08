from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import labs

# 序列化相关
from rest_framework.viewsets import ModelViewSet
from .serializers import labSerializer

# 序列化
class labAPIView(ModelViewSet):
    queryset = labs.objects.all()
    serializer_class = labSerializer