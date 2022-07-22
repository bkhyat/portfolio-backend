from rest_framework import viewsets, status
from rest_framework.response import Response

from api.todo.v1.serializers import ToDoSerializer
from todo.models import ToDo


class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
