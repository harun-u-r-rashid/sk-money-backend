from django.contrib import admin
from django.urls import path
from . import views

from rest_framework_simplejwt.views import TokenRefreshView




urlpatterns = [
    #    User authentication
    path("register/", views.RegisterView.as_view()),
    path("verify/", views.VerifyUserView.as_view()),
    path("login/", views.LoginView.as_view()),

    # path("logout/", views.LogoutView.as_view()),
    # path("refresh/", TokenRefreshView.as_view()),
    path("user_search/", views.SearchUserView.as_view()),
    path("user_details/<int:id>/", views.UserDetailsView.as_view()),
]


