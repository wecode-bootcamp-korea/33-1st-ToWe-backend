from django.urls import path

from .views import SignupView, LoginView, MyPageView

urlpatterns = [
    path("/signup", SignupView.as_view()),
    path("/login", LoginView.as_view()),
    path("/mypage", MyPageView.as_view())
]