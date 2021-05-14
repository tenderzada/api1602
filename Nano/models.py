from django.db import models
# 导入内建的User模型。
from django.contrib.auth.models import User
# timezone 用于处理时间相关事务。
from django.utils import timezone
from PIL import Image
# 引入imagekit
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
# dingtalk
from django.db import models

'''
表1 receiver(主键) dingding-webhook
表2 自增ID alertname instance anomaly_img startsAt receiver longitude latitude
'''

class Receiver(models.Model):
    receiver = models.CharField(max_length=30)
    receiver_num = models.IntegerField()
    dingtalk_robot_api = models.CharField(max_length=200)

    class Meta:
        db_table = 'receiver'
        unique_together = ('receiver', 'receiver_num')


class Alert(models.Model):
    id = models.AutoField(primary_key=True)
    alertname = models.CharField(max_length=100)
    instance = models.CharField(max_length=50)
    anomaly_img = models.URLField()
    startsAt = models.DateTimeField()
    receiver = models.CharField(max_length=30)
    longitude = models.CharField(max_length=30)
    latitude = models.CharField(max_length=30)

    class Meta:
        db_table = 'alert'
