from django.urls import include, path
from api.resume.urls import urlpatterns as resume_url

urlpatterns = [
    path(r'resume/', include(resume_url))
]