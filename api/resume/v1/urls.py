from rest_framework.routers import SimpleRouter

from api.resume.v1.profile.views import ProfileViewSet
from api.resume.v1.experience.views import ExperienceViewSet

router = SimpleRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'experiences', ExperienceViewSet)

urlpatterns = router.urls