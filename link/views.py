# from django.shortcuts import render
# from django.shortcuts import render
# from django.shortcuts import render
# from django.shortcuts import get_object_or_404
# from rest_framework.decorators import api_view

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from user.models import Interest
from fuzzywuzzy import fuzz
from django.db.models import *

# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renders import JSONRenderer
# from rest_framework.parsers import JSONParser
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


# course get on the basis of interest of the session user and post done
# todo validation left

class CourseList(APIView):
    def get_object(self, user):
        return Interest.objects.filter(user=user)

    def get(self, request, id):
        interest = self.get_object(id)
        i = []
        c_serializer = []
        # summing up interest
        for val in interest:
            i.append(val.name)
        #summing up all courses according to each interest
        c = Course.objects.all()

        for val in i:
            for x in c:
                if fuzz.partial_ratio(val,x.description) > 80:
                    c_serializer.append({"name":x.name,"category":x.category,"founder":x.founder,"description":x.description})

        return Response(c_serializer)

    def post(self, request, id):
        c_serializer = courseSerializer(data=request.data)
        if c_serializer.is_valid():
            c_serializer.save()
            return Response(content, status=status.HTTP_201_CREATED)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


# module created and retrieve
# todo validation left

class ModuleList(APIView):
    def get(self, request):
        module = Module.objects.all()
        m_serializer = moduleSerializer(module, many=True)
        return Response(m_serializer.data)

    def post(self, request):
        m_serializer = moduleSerializer(data=request.data)
        if m_serializer.is_valid():
            m_serializer.save()
            return Response(content, status=status.HTTP_201_CREATED)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


class EnrollList(APIView):
    def get_object(self,user):
        return Enrollment.objects.filter(user = user)

    def get(self, request, id):
        enroll = self.get_object(id)
        e_serializer = enrollSerializer(enroll, many=True)
        for val in e_serializer.data:
            val['course_name'] = Course.objects.get(id = val['course_enrolled']).name
        return Response(e_serializer.data)

    def post(self, request, id):
        e_serializer = enrollSerializer(data=request.data)
        if e_serializer.is_valid():
            e_serializer.save()
            return Response(content, status=status.HTTP_201_CREATED)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)

# course analysis
class course_analysisList(APIView):

    def get(self,request):
        x = Enrollment.objects.values('course_enrolled').annotate(count=Count('user')).distinct()
        for val in x:
            val["course_name"] = Course.objects.get(pk = val['course_enrolled']).name
        return Response(x)

class student_analysisList(APIView):

    def get(self,request):
        pass
    def post(self,request):
        pass