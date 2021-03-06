from rest_framework import viewsets, status
from rest_framework.response import Response

from api.todo.v1.serializers import ToDoSerializer
from todo.models import ToDo


class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    def create(self, request, *args, **kwargs):
        is_many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=is_many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
