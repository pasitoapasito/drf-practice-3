from django.urls import path
from users.views import UserSignUpView, UserSignOutView, UserinfoView 

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('/signup', UserSignUpView.as_view()),
    path('/signin', TokenObtainPairView.as_view()),
    path('/signout', UserSignOutView.as_view()),
    path('/auth', UserinfoView.as_view()),
    path('/token/refresh', TokenRefreshView.as_view()),
]
