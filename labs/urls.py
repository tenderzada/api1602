# in pollsapi/urls.py
from django.contrib import admin
from django.urls import path, include

#drf
from rest_framework.routers import DefaultRouter
from .views import labAPIView


urlpatterns = [
]

router = DefaultRouter()
router.register("", labAPIView)
urlpatterns += router.urls