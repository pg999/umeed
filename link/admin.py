from django.contrib import admin
from .models import *

admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Enrollment)
admin.site.register(Test)
admin.site.register(Marks)
# Register your models here.
