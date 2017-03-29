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

class aspirantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aspirant
        # fields=('ticker','open','volume')
        fields = '__all__'

class loginSerializer(serializers.ModelSerializer):
    def xyz(self, data):
        content[0]['id'] = 0
        x = Aspirant.objects.filter(email=data['email'])
        if x:
            temp = Aspirant.objects.get(email=data['email'])
            if data['password'] == temp.password :
                content[0]['id'] = temp.id
        return content


    class Meta:
        model = Aspirant
        fields = ('email','password')

class interestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Interest
        fields='__all__'

class locationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Locations
        fields='__all__'

class aspirantskillSerializer(serializers.ModelSerializer):
    class Meta:
        model=Aspirant_skill
        fields='__all__'