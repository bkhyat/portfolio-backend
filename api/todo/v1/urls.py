from rest_framework.routers import SimpleRouter

from api.todo.v1.viewsets import ToDoViewSet

router = SimpleRouter()
router.register('todos', ToDoViewSet)

urlpatterns = router.urls