from django.urls import path
from users.views import UserSignupView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('/signup', UserSignupView.as_view()),
    path('/token', TokenObtainPairView.as_view()),
    path('/token/refresh', TokenRefreshView.as_view()),
]
