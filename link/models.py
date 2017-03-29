from __future__ import unicode_literals
from django.db import models
from user.models import Aspirant


class Course(models.Model):
    founder = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, null=True)
    detail = models.CharField(max_length=1000, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return str(self.id)


class Module(models.Model):
    main_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    module_name = models.CharField(max_length=200, blank=True, null=True)
    module_description = models.CharField(max_length=700, blank=True, null=True)
    video_path = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.main_course)


class Enrollment(models.Model):
    course_enrolled = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(Aspirant, on_delete=models.CASCADE)
    enrolled_on = models.DateField(auto_now_add=True)
    completion = models.FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.user)

class Test(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    question = models.CharField(max_length=1000)
    option1 =models.CharField(max_length=1000)
    option2 =models.CharField(max_length=1000)
    option3 =models.CharField(max_length=1000)
    option4 =models.CharField(max_length=1000)
    answer =models.IntegerField()

class Marks(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    user = models.ForeignKey(Aspirant, on_delete=models.CASCADE)
    marks = models.IntegerField(default=0)

    def __str__(self):
        return str(self.module)
