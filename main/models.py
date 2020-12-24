from django.db import models

# Create your models here.

class lab(models.Model):
    # 实验室名称
    labId = models.CharField(max_length = 100)
    # 实验室介绍
    lab_description = models.CharField(max_length=200)

    def __str__(self):
        return self.labId
