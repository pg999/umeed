from rest_framework import serializers

from .models import *
import base64
from django.core.files.base import ContentFile

content = [
    {
        'error': 0,
        'response': 'success',
        'id': 0
    }
]
error = [
    {
        'error': 1,
        'response': 'fail',
        'id': 0
    }
]

class courseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields='__all__'

class moduleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Module
        fields='__all__'

class enrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'

class testSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'

class marksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marks
        fields = '__all__'