from __future__ import unicode_literals
from django.db import models


# Create your models here.


class Aspirant(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=40, blank=True, null=True)
    education = models.CharField(max_length=40, blank=True, null=True)
    account_no = models.CharField(max_length=40, blank=True, null=True)
    dob = models.DateField(max_length=30, null=True, blank=True)
    password = models.CharField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    # location = models.CharField(max_length=1000, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    gender = models.CharField(max_length=30, blank=True, null=True)
    date_of_joining = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class Interest(models.Model):
    user = models.ForeignKey(Aspirant, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Aspirant_skill(models.Model):
    user = models.ForeignKey(Aspirant, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, null=True, blank=True)
    percentage = models.FloatField(max_length=5 , null=True, default=0.0)
    acquired_date = models.DateField(max_length=30, null=True, blank=True)

    def __str__(self):
        return str(self.user)
