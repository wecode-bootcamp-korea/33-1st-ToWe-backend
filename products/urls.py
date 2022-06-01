from django.urls import path

from products.views import LikeView, ProductDetailView, ProductListView, ReviewView

urlpatterns = [
    path('/<int:product_id>', ProductDetailView.as_view()),
    path('', ProductListView.as_view()),
    path("/review", ReviewView.as_view()),
    path('/<int:product_id>/like', LikeView.as_view()) 
]