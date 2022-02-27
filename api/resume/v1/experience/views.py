from rest_framework.viewsets import ReadOnlyModelViewSet

from api.resume.v1.experience.serializers import ExperienceSerializer
from resume.models import Experience


class ExperienceViewSet(ReadOnlyModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
