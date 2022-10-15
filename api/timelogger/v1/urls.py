from django.urls import path, include
from rest_framework.routers import SimpleRouter

from api.timelogger.v1.viewsets import TimeLoggerViewSet

router = SimpleRouter()
router.register(r'', TimeLoggerViewSet, basename='TimeLog')

urlpatterns = router.urls

