from django.urls import include, path

from api.todo.v1.urls import urlpatterns as v1URL

urlpatterns = [
    path('v1/', include(v1URL))
]