# from django.shortcuts import get_object_or_404
# from rest_framework.decorators import api_view
from itertools import chain

from link.models import Enrollment
from link.serializers import enrollSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.serializers import *

from .serializers import *

# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser

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


# company created and retrieve
# validation left

class CompanyList(APIView):
    def get(self, request):
        company = Company.objects.all()
        c_serializer = companySerializer(company, many=True)
        return Response(c_serializer.data)

    # company signup

    def post(self, request):
        c_serializer = companySerializer(data=request.data)
        if c_serializer.is_valid():
            c_serializer.save()
            content[0]['id'] = c_serializer.data['id']
            return Response(content, status=status.HTTP_201_CREATED)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)

        # todo put method for partial updation


# company profile editable
# todo validations
class Company_ProfileList(APIView):
    def get_object(self, pk):
        return Company.objects.get(pk=pk)

    def get(self, request, id):
        company = Company.objects.get(id=id)
        c_serializer = companySerializer(company)
        return Response(c_serializer.data)

    def patch(self, request, id, format=None):
        company = self.get_object(id)
        c_serializer = companySerializer(company, data=request.data, partial=True)
        if c_serializer.is_valid():
            c_serializer.save()
            return Response(content, status=status.HTTP_201_CREATED)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)

# jobs created and retrieve
# todo validation

class JobList(APIView):
    # 1.last_apply()
    # 2.location
    # 3.vacancies
    # 4.stipend
    # 5.skill required

    def get_object(self, pre):
        if pre == "1":
            return Job.objects.order_by('-last_date')
        elif pre == "2":
            # todo matching with user location
            return Job.objects.order_by('location')
        elif pre == "3":
            return Job.objects.order_by('-vacancies')
        elif pre == "4":
            return Job.objects.order_by('-stipend')
        else:
            return Job.objects.all()
            # elif pre == 5:
            #     return Job.objects.order_by()

            # view all jobs

    def get(self, request, pre):
        jobs = self.get_object(pre)
        j_serializer = jobSerializer(jobs, many=True)
        for val in j_serializer.data:
            val['company_name'] = Company.objects.get(id=val['company_from']).company_name
        return Response(j_serializer.data)

    # post a job

    def post(self, request, pre):
        d = request.data
        j_serializer = jobSerializer(data=d)
        if j_serializer.is_valid():
            j_serializer.save()
            content[0]['id'] = j_serializer.data['id']
            x = Company.objects.get(id=request.data['company_from']).category
            Job.objects.filter(pk=content[0]['id']).update(category=x)
            return Response(content, status=status.HTTP_201_CREATED)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


# get a particular job and apply for it

class jobs_id_List(APIView):
    def get_object(self, pk):
        return Job.objects.get(pk=pk)

    # get a particular job
    def get(self, request, pk):
        job_id = self.get_object(pk)
        j_serializer = jobSerializer(job_id)
        return Response(j_serializer.data)

    # enter skills required in a particular job
    #     a = [{
    #         "job_id":xyz,
    #         "user_id":abc,
    #     }]
    def post(self, request, pk):
        j_id_serializer = jobappliedSerializer(data=request.data)
        if j_id_serializer.is_valid():
            j_id_serializer.save()
            return Response(content, status=status.HTTP_201_CREATED)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        job = self.get_object(pk)
        j_serializer = jobSerializer(job, data=request.data)
        if j_serializer.is_valid():
            j_serializer.save()
            return Response(content, status=status.HTTP_201_CREATED)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


# jobskill created and retrieve
# todo validation left

class jobskillList(APIView):
    def get_object(self, job_from):
        return Job_skills.objects.filter(job_from=job_from)

    def get(self, request, id):
        job_skills = self.get_object(id)
        j_s_serializer = jobskillSerializer(job_skills, many=True)
        return Response(j_s_serializer.data)

    # enter skills required in a particular job

    def post(self, request, id):
        j_s_serializer = jobskillSerializer(data=request.data)
        if j_s_serializer.is_valid():
            j_s_serializer.save()
            return Response(content, status=status.HTTP_201_CREATED)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


# all the applied user for a particular job

class user_applied_List(APIView):
    def get_object(self, company_from):
        return Job.objects.filter(company_from=company_from)

    def get(self, request, id):
        user = []
        jobs = self.get_object(id)

        for job in jobs:
            job_app = job_applied.objects.filter(job=int(job.id)).order_by("-date_applied")
            for j in job_app:
                user = list(chain(user, Aspirant.objects.filter(pk=j.user.id)))

        u_serializer = aspirantSerializer(user, many=True)
        for val in u_serializer.data:
            skills = Aspirant_skill.objects.filter(user=val['id'])
            s_serializer = aspirantskillSerializer(skills, many=True)
            enroll = Enrollment.objects.filter(user=val['id'])
            e_serializer = enrollSerializer(enroll, many=True)
            val["Enrolled in courses"] = e_serializer.data
            val["Skill Gained"] = s_serializer.data

        return Response(u_serializer.data)

        # def post(self,request,id):
        #     pass


class Company_job_List(APIView):
    # get a particular job
    def get(self, request, pk):
        jobs = Job.objects.filter(company_from=pk).order_by("date_of_posting")
        j_serializer = jobSerializer(jobs, many=True)
        return Response(j_serializer.data)

    def post(self, request, id):
        pass
