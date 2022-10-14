from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView

urlpatterns = [
    path('v1/login/', TokenObtainPairView.as_view()),
    path('v1/refresh/', TokenRefreshView.as_view()),
    path('v1/logout/', TokenBlacklistView.as_view())
]