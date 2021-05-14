# 引入表单类
from django import forms
# 引入文章模型
from .models import Alert

# Alert表单类
class AlertForm(forms.ModelForm):
    class Meta:
        model = Alert
        fields = ('alertname', 'instance', 'anomaly_img', 'startsAt', 'receiver', 'longitude', 'latitude')