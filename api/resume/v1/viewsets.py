from django.contrib.auth.models import User
from rest_framework import views, viewsets, generics

from api.resume.v1.serializers import ResumeSerializer


class ResumeViewSet(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = ResumeSerializer
