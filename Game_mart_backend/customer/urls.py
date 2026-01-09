from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView
from . import views


urlpatterns = [
        path("account/", views.account_overview, name="overview"),
        path("account/register", views.RegisterView, name="register"),
        path("account/login", TokenObtainPairView.as_view(), name="login"),
        path("account/refresh", TokenRefreshView.as_view(), name="refresh"),
        path("account/logout", TokenBlacklistView.as_view(), name="logout"),
        path("account/detail", views.CurrentUserDetail, name="user_detail"),
        path("account/update", views.Upadte_Customer, name="user_update"),
]