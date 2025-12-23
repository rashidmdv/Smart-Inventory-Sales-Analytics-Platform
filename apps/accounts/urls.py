from django.urls import path
from .views.auth_view import RegisterView, LoginView
from apps.accounts.views.user_managment import UserManagementView

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("login/", LoginView.as_view()),
    path("user-managment/",UserManagementView.as_view())
]
