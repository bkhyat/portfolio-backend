from django.urls import path, include

urlpatterns = [path(r"v1/", include("api.auth.v1.urls"))]