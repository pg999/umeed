from django.conf.urls import url,include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from user import views
from  link.views import CourseList,ModuleList, EnrollList, course_analysisList
from  industry.views import *
from django.conf import settings
from django.conf.urls.static import static
from user.views import ProfileList, job_trendList

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^aspirant/$', views.AspirantsList.as_view()),
    url(r'^login/$', views.LoginList.as_view()),
    url(r'^course/(?P<id>[0-9]+)/$', CourseList.as_view()),
    url(r'^module/$', ModuleList.as_view()),
    url(r'^interest/(?P<id>[0-9]+)/$', views.InterestList.as_view()),
    url(r'^company/$', CompanyList.as_view()),
    url(r'^jobs/(?P<pre>[0-9]+)/$', JobList.as_view()),
    url(r'^jobskill/(?P<id>[0-9]+)/$', jobskillList.as_view()),
    url(r'^jobid/(?P<pk>[0-9]+)/$', jobs_id_List.as_view()),
    url(r'^userapld/(?P<id>[0-9]+)/$', user_applied_List.as_view()),
    url(r'^enroll/(?P<id>[0-9]+)/$', EnrollList.as_view()),
    url(r'^profile/(?P<pk>[0-9]+)/$', ProfileList.as_view()),
    url(r'^jobtrend/$', job_trendList.as_view()),
    url(r'^coursetrend/$', course_analysisList.as_view()),
    url(r'^companyprofile/(?P<id>[0-9]+)/$', Company_ProfileList.as_view()),
]
