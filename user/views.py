from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from industry.models import Job
from link.models import Enrollment
from link.serializers import enrollSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Aspirant
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.db.models import *

# Create your views here.
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

# Registration of the user
# todo validation left
class AspirantsList(APIView):

    @staticmethod
    def get(request):
        aspirants = Aspirant.objects.all()
        a_serializer = aspirantSerializer(aspirants, many=True)
        return Response(a_serializer.data)

    @staticmethod
    def post(request):
        a_serializer = aspirantSerializer(data=request.data)
        if a_serializer.is_valid():
            a_serializer.save()
            return Response(content, status=status.HTTP_201_CREATED)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)

#todo put method
class ProfileList(APIView):

    def get_object(self,pk):
        return Aspirant.objects.get(pk = pk)

    def get(self, request, pk):
        user = self.get_object(pk)
        skills = Aspirant_skill.objects.filter(user = user.id)
        s_serializer = aspirantskillSerializer(skills, many=True)
        enroll = Enrollment.objects.filter(user = user.id)
        e_serializer = enrollSerializer(enroll,many=True)
        result = [{
            "name":user.name,
            "address":user.address,
            "dob":user.dob,
            "email":user.email,
            "account_no":user.account_no,
            "Enrolled in courses":e_serializer.data,
            "Skill Gained":s_serializer.data
        }]
        return Response(result)

    def put(self, request, pk, format = None):
        user = self.get_object(pk)
        u_serializer = aspirantSerializer(user,data=request.data)
        if u_serializer.is_valid():
            u_serializer.save()
            return Response(content, status=status.HTTP_200_OK)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


class job_trendList(APIView):

    def get(self,request):
        x = Job.objects.values('category').annotate(count=Count('category')).distinct()
        return Response(x)

# login of the aspirant (user)
# todo validation left

class LoginList(APIView):
    def get(self,request):
        return Response()

    def post(self,request):
        l = loginSerializer(data=request.data)
        content = l.xyz(data=request.data)
        if content[0]['id'] != 0:
            return Response(content, status=status.HTTP_200_OK)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)

# adding multiple interest
# todo validation left and put method
class InterestList(APIView):
    def get_object(self, user):
        return Interest.objects.filter(user = user)

    def get(self,request, id):
        interest = self.get_object(id)
        i_serializer = interestSerializer(interest,many=True)
        return Response(i_serializer.data)

    def post(self,request, id):
        data =request.data
        data["user"] = id
        i_serializer = interestSerializer(data=data)
        if i_serializer.is_valid():
            i_serializer.save()
            return Response(content, status=status.HTTP_200_OK)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)

