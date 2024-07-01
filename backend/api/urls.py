from api import views as api_views
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("user/token", api_views.MyTokenObtainPairView.as_view()),
    path("user/token/refresh/", TokenRefreshView.as_view()),
    path("user/register/", api_views.RegisterView.as_view()),
    path("user/passowrd-reset/<email>/", api_views.PasswordResetVerifyAPIView.as_view()),
    path("user/passowrd-change/", api_views.PasswordChangeAPIView.as_view()),
]
