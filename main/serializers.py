from rest_framework import serializers

from .models import lab

class labSerializer(serializers.ModelSerializer):
    class Meta:
        model = lab
        fields = '__all__'

    