from django.db.models import *
from fuzzywuzzy import fuzz
from industry.models import Job, Company
from link.models import Enrollment, Course, NGO
from link.serializers import enrollSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *

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

    # ---------------------------------------------------------------------------------signup
    @staticmethod
    def post(request):
        a_serializer = aspirantSerializer(data=request.data)
        if a_serializer.is_valid():
            a_serializer.save()
            content[0]['id'] = a_serializer.data['id']
            return Response(content, status=status.HTTP_201_CREATED)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


# ----------------------------------------------------------------------get profile
# todo put method
class ProfileList(APIView):
    def get_object(self, pk):
        return Aspirant.objects.get(pk=pk)

    def get(self, request, pk):
        user = self.get_object(pk)
        skills = Aspirant_skill.objects.filter(user=user.id)
        s_serializer = aspirantskillSerializer(skills, many=True)
        enroll = Enrollment.objects.filter(user=user.id)
        e_serializer = enrollSerializer(enroll, many=True)
        result = [{
            "name": user.name,
            "address": user.address,
            "dob": user.dob,
            "email": user.email,
            "education": user.education,
            "account_no": user.account_no,
            "phone": user.phone,
            "Enrolled in courses": e_serializer.data,
            "Skill Gained": s_serializer.data
        }]
        return Response(result)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        u_serializer = aspirantSerializer(user, data=request.data)
        if u_serializer.is_valid():
            u_serializer.save()
            return Response(content, status=status.HTTP_200_OK)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


class job_trendList(APIView):
    def get(self, request):
        x = Job.objects.values('category').annotate(count=Count('category')).distinct()
        return Response(x)


# login of the aspirant (user)
# todo validation left

class LoginList(APIView):
    def get(self, request):
        return Response()

    def post(self, request):
        data = request.data
        result = [
            {
                'error': 0,
                'response': 'success'
            }
        ]
        email = data['email']
        password = data['password']
        x = Aspirant.objects.filter(email=email, password=password)
        if x:
            result[0]['a_id'] = x[0].id
            return Response(result, status=status.HTTP_200_OK)
        x = Company.objects.filter(email=email, password=password)
        if x:
            result[0]['c_id'] = x[0].id
            return Response(result, status=status.HTTP_200_OK)
        x = NGO.objects.filter(email=email, password=password)
        if x:
            result[0]['n_id'] = x[0].id
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)


# adding multiple interest
# todo validation left and put method
class InterestList(APIView):
    def get_object(self, user):
        return Interest.objects.filter(user=user)

    def get(self, request, id):
        interest = self.get_object(id)
        i_serializer = interestSerializer(interest, many=True)
        return Response(i_serializer.data)

    def post(self, request, id):
        data = request.data
        Interest.objects.filter(user=id).delete()
        for d in data:
            d["user"] = id
            i_serializer = interestSerializer(data=d)
            if i_serializer.is_valid():
                i_serializer.save()
                # return Response(content, status=status.HTTP_200_OK)
        return Response(content, status=status.HTTP_200_OK)


class LocationList(APIView):
    def get_object(self, user):
        return Locations.objects.filter(user=user)

    def get(self, request, id):
        location = self.get_object(id)
        l_serializer = locationSerializer(location, many=True)
        return Response(l_serializer.data)

    def post(self, request, id):
        data = request.data
        Locations.objects.filter(user=id).delete()
        for d in data:
            d["user"] = id
            l_serializer = locationSerializer(data=d)
            if l_serializer.is_valid():
                l_serializer.save()
                # return Response(content, status=status.HTTP_200_OK)
        return Response(content, status=status.HTTP_200_OK)


class searchCourse(APIView):
    def get(self, request):
        return Response("search karobey")

    def post(self, request):
        data = request.data

        search = data['search']
        i = []
        course = Course.objects.all()
        for x in course:
            if fuzz.partial_ratio(search, x.description) > 80:
                i.append({"id": x.id, "name": x.name, "category": x.category, "founder": x.founder,
                          "description": x.description})
        return Response(i)


class searchJob(APIView):
    def get(self, request):
        return Response("search karobey")

    def post(self, request):
        data = request.data
        search = data['search']
        i = []
        job = Job.objects.all()
        for x in job:
            if fuzz.partial_ratio(search, x.description) > 80:
                i.append({"id": x.id, "company_from": x.company_from, "title": x.title, "description": x.description,
                          "vacancies": x.vacancies,
                          "category": x.category, "stipend": x.stipend})
        return Response(i)
