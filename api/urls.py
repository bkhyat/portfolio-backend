from django.urls import include, path
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.resume.urls import urlpatterns as resume_url
from api.todo.urls import urlpatterns as todo_url
from api.auth.urls import urlpatterns as auth_url
from api.timelogger.urls import urlpatterns as timelogger_url


@api_view()
def get_requirements(request):
    req_file = open('requirements.txt', 'r')
    return Response([{"library": x[0], "version": x[1]} for line in req_file for x in [line.strip('\n').split('==')]])


urlpatterns = [
    path(r'resume/', include(resume_url)),
    path(r'todo/', include(todo_url)),
    path(r'requirements/', get_requirements),
    path(r'auth/', include(auth_url)),
    path(r'time-logger/', include(timelogger_url)),
]
