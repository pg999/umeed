from django.db import models
from user.models import Interest, Aspirant


class Company(models.Model):
    founder = models.CharField(max_length=100, blank=False, null=False)
    company_name = models.CharField(max_length=40, blank=True, null=True)
    company_address = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=40, blank=True, null=True)
    employee_count = models.CharField(max_length=40, blank=True, null=True)
    company_introduction = models.CharField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(max_length=200, blank=False, null=False)
    mobile = models.CharField(max_length=15, blank=False, null=False)

    def __str__(self):
        return str(self.id)


class Job(models.Model):
    company_from = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, null=True)
    date_of_posting = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    vacancies = models.IntegerField(blank=True, null=True)
    last_date = models.DateField(max_length=30, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    stipend = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.company_from)


class Job_skills(models.Model):
    job_from = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return str(self.job_from)


class job_applied(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(Aspirant, on_delete=models.CASCADE)
    date_applied = models.DateField(max_length=30, auto_now_add=True)
    selected = models.BooleanField(default=False)

    def __str__(self):
        return str(self.job)
