from rest_framework import routers

from api.vocab.v1.viewsets import VocabViewset, PageViewset

router = routers.SimpleRouter()
router.register("sources", VocabViewset)
router.register("pages", PageViewset)

urlpatterns = router.urls