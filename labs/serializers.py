from rest_framework import serializers

from .models import labs

class labSerializer(serializers.ModelSerializer):
    class Meta:
        model = labs
        fields = '__all__'

    