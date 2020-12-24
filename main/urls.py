# in pollsapi/urls.py
from django.contrib import admin
from django.urls import path, include
from .views import labs_list,labs_detail

#drf
from rest_framework.routers import DefaultRouter
from .views import labAPIView


urlpatterns = [
    # path('labs/', labs_list, name = "labs_list"),
    # path('labs/<int:pk>/', labs_detail, name = "labs_detail"),
]

router = DefaultRouter()
router.register("labs", labAPIView)
urlpatterns += router.urls