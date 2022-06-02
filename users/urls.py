from django.urls import path

from .views import SignupView, LoginView, UserInfoView, UserReviewView

urlpatterns = [
    path("/signup", SignupView.as_view()),
    path("/login", LoginView.as_view()),
    path("/info", UserInfoView.as_view()),
    path("/reviews", UserReviewView.as_view())
]