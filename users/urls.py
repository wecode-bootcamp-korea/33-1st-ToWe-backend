from django.urls import path

from .views import SignupView, LoginView, UserDetailView, LikeView

urlpatterns = [
    path("/signup", SignupView.as_view()),
    path("/login", LoginView.as_view()),
    path("/detail", UserDetailView.as_view()),
    path("/like", LikeView.as_view())
]