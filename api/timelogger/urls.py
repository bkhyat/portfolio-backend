from django.urls import path, include

from api.timelogger.v1.urls import urlpatterns as v1_url

urlpatterns = [path(r"v1/", include(v1_url))]