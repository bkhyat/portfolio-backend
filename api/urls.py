from django.urls import include, path
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.resume.urls import urlpatterns as resume_url


@api_view()
def get_requirements(request):
    req_file = open('requirements.txt', 'r')
    return Response([{"library": x[0], "version": x[1]} for line in req_file for x in [line.strip('\n').split('==')]])


urlpatterns = [
    path(r'resume/', include(resume_url)),
    path(r'requirements/', get_requirements)
]
