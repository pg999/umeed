# from django.shortcuts import render
# from django.shortcuts import render
# from django.shortcuts import render
# from django.shortcuts import get_object_or_404
# from rest_framework.decorators import api_view

from django.db.models import *
from fuzzywuzzy import fuzz
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import Interest

from .serializers import *

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
        c = Course.objects.filter(online=True)
        c_l_serializer = courseSerializer(c, many=True)
        # summing up all courses according to each interest
        for val in i:
            for x in c:
                if fuzz.partial_ratio(val, x.description) > 80:
                    c_serializer.append(
                        {"id": x.id, "name": x.name, "category": x.category, "founder": x.founder,
                         "description": x.description})
        result = [{
            "matching interest": c_serializer,
            "all interest": c_l_serializer.data
        }]
        return Response(result)

    def post(self, request, id):
        c_serializer = courseSerializer(data=request.data)
        if c_serializer.is_valid():
            c_serializer.save()
            return Response(content, status=status.HTTP_201_CREATED)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


class WorkshopList(APIView):
    def get_object(self, user):
        return Interest.objects.filter(user=user)

    def get(self, request, id):
        interest = self.get_object(id)
        i = []
        c_serializer = []
        # summing up interest
        for val in interest:
            i.append(val.name)
        c = Course.objects.filter(online=False)
        c_l_serializer = courseSerializer(c, many=True)
        # summing up all courses according to each interest
        for val in i:
            for x in c:
                if fuzz.partial_ratio(val, x.description) > 80:
                    c_serializer.append(
                        {"id": x.id, "name": x.name, "category": x.category, "founder": x.founder,
                         "description": x.description})
        result = [{
            "matching interest": c_serializer,
            "all interest": c_l_serializer.data
        }]
        return Response(result)


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
    def get_object(self, user):
        return Enrollment.objects.filter(user=user)

    def get(self, request, id):
        enroll = self.get_object(id)
        e_serializer = enrollSerializer(enroll, many=True)
        for val in e_serializer.data:
            val['course_name'] = Course.objects.get(id=val['course_enrolled']).name
        return Response(e_serializer.data)

    def post(self, request, id):
        e_serializer = enrollSerializer(data=request.data)
        if e_serializer.is_valid():
            e_serializer.save()
            x = Aspirant.objects.get(id=request.data['user']).location
            Enrollment.objects.filter(pk=e_serializer.data['id']).update(location=x)
            return Response(content, status=status.HTTP_201_CREATED)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


# course analysis
class course_analysisList(APIView):
    def get(self, request):
        x = Enrollment.objects.values('course_enrolled').annotate(count=Count('user')).distinct()
        for val in x:
            val["course_name"] = Course.objects.get(pk=val['course_enrolled']).name
        return Response(x)


class student_analysisList(APIView):
    def get(self, request):
        # data = request.data
        value = Enrollment.objects.filter(location='Lucknow').values('course_enrolled').annotate(count=Count('user'))
        for val in value:
            val['course_name'] = Course.objects.get(pk=val['course_enrolled']).name
        return Response(value)


class course_moduleList(APIView):
    def get_object(self, id):
        return Course.objects.get(id=id)

    def get(self, request, id):
        course = self.get_object(id)
        c_serializer = courseSerializer(course)
        module = Module.objects.filter(main_course=id)
        m_serializer = moduleSerializer(module, many=True)
        c_serializer.data['modules'] = m_serializer.data
        return Response(m_serializer.data)  # changed

    def put(self, request, id, foramt=None):
        course = self.get_object(id)
        c_serializer = courseSerializer(course, data=request.data)
        if c_serializer.is_valid():
            c_serializer.save()
            return Response(content, status=status.HTTP_201_CREATED)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


class module_idList(APIView):
    def get_object(self, pk):
        return Module.objects.get(pk=pk)

    def get(self, request, pk):
        module = self.get_object(pk)
        m_serializer = moduleSerializer(module)
        return Response(m_serializer.data)

    def put(self, request, pk, format=None):
        module = self.get_object(pk)
        m_serializer = moduleSerializer(module, data=request.data)
        if m_serializer.is_valid():
            m_serializer.save()
            return Response(content, status=status.HTTP_201_CREATED)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


class testList(APIView):
    def get_object(self, module):
        return Test.objects.filter(module=module)

    def get(self, request, id):
        test = self.get_object(id)
        t_serializer = testSerializer(test, many=True)
        return Response(t_serializer.data)

    def post(self, request):
        t_serializer = testSerializer(data=request.data)
        if t_serializer.is_valid():
            t_serializer.save()
            return Response(content, status=status.HTTP_201_CREATED)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


class marksList(APIView):
    def get(self, request, moduleid, userid):
        mark = Marks.objects.all()
        m_serializer = marksSerializer(mark, many=True)
        return Response(m_serializer.data)

    # [{
    #    "module":moduleid,
    #     "user":userid,
    #     "marks":marks
    # }]
    def post(self, request, moduleid, userid):
        m_serializer = marksSerializer(data=request.data)
        if m_serializer.is_valid():
            m_serializer.save()
            return Response(content, status=status.HTTP_201_CREATED)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


class ngo(APIView):
    def get(self, request):
        u = NGO.objects.all()
        u_serializer = NGOSerializer(u, many=True)

        return Response(u_serializer.data)

    def post(self, request):
        n_serializer = NGOSerializer(data=request.data)
        if n_serializer.is_valid():
            n_serializer.save()
            content[0]['id'] = n_serializer.data['id']
            return Response(content, status=status.HTTP_201_CREATED)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


class NProfileList(APIView):
    def get_object(self, pk):
        return NGO.objects.get(pk=pk)

    def get(self, request, pk):
        user = self.get_object(pk)
        u_serializer = NGOSerializer(user)
        return Response(u_serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        u_serializer = NGOSerializer(user, data=request.data)
        if u_serializer.is_valid():
            u_serializer.save()
            return Response(content, status=status.HTTP_200_OK)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


class loadcourses(APIView):
    def get(self, request):
        course = Course.objects.all()
        c_serializer = courseSerializer(course, many=True)
        return Response(c_serializer.data)
