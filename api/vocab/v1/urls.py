from rest_framework import routers

from api.vocab.v1.viewsets import VocabViewset, PageViewset, WordViewset, VocabPracticeViewset

router = routers.SimpleRouter()
router.register("sources", VocabViewset)
router.register("pages", PageViewset)
router.register("words", WordViewset)
router.register("practice", VocabPracticeViewset)


urlpatterns = router.urls