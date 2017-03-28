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

class companySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields='__all__'

class signupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('founder','email','password','mobile')

class loginSerializer(serializers.ModelSerializer):
    def xyz(self, data):
        content[0]['id'] = 0
        x = Company.objects.filter(email=data['email'])
        if x:
            temp = Company.objects.get(email=data['email'])
            if data['password'] == temp.password :
                content[0]['id'] = temp.id
        return content

    class Meta:
        model = Company
        fields = ('email','password')

class jobSerializer(serializers.ModelSerializer):
    class Meta:
        model=Job
        fields='__all__'

class jobskillSerializer(serializers.ModelSerializer):
    class Meta:
        model=Job_skills
        fields='__all__'

class jobappliedSerializer(serializers.ModelSerializer):
    class Meta:
        model=job_applied
        fields='__all__'