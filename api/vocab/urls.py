from django.urls import path, include
from api.vocab.v1.urls import urlpatterns as v1_urls
urlpatterns = [
    path("v1/", include(v1_urls))
]