from django.urls import path

from products.views import ProductDetailView, ReviewView

urlpatterns = [
    path('/<int:product_id>', ProductDetailView.as_view()),
    path("/review", ReviewView.as_view())
]