from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import lab

# 序列化相关

from rest_framework.viewsets import ModelViewSet
from .serializers import labSerializer


def labs_list(request):
    MAX_OBJECTS = 20
    labs = lab.objects.all()[:MAX_OBJECTS]  # 从lab模型（对应数据库中的表）中取出前20条记录
    data = {"results": list(labs.values("labId", "lab_description"))}  # 以dict形式组织数据
    return JsonResponse(data)  # JsonResponse与Django的HttpResponse类似，但它响应的content-type=application/json.
  

def labs_detail(request, pk):
    lab_detail = get_object_or_404(lab, pk=pk)  # 获取对象实例或返回404状态
    print(lab_detail)
    data = {"results": {
        "labId": lab_detail.labId,
        "lab_description": lab_detail.lab_description,
    }}
    return JsonResponse(data)

# 序列化

class labAPIView(ModelViewSet):
    queryset = lab.objects.all()
    serializer_class = labSerializer