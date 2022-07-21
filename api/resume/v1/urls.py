from django.urls import path

from api.resume.v1.viewsets import ResumeViewSet

urlpatterns = [
    path(r'users/<int:pk>/', ResumeViewSet.as_view())
]