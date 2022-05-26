from django.urls import path

from .views import LoginView, SignupView, MypageView

urlpatterns = [
    path("/signup", SignupView.as_view()),
    path("/login", LoginView.as_view()),
    path("/mypage", MypageView.as_view()),
]