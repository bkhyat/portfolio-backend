from django.urls import include, path
from api.resume.v1.urls import urlpatterns as v1URL

urlpatterns = [
    path(r'v1/', include(v1URL))
]