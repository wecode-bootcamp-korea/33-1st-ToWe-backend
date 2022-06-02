from django.urls import path

from products.views import ProductDetailView, ProductListView, ReviewView

urlpatterns = [
    path('', ProductListView.as_view()),
    path('/<int:product_id>', ProductDetailView.as_view()),
    path('/<int:product_id>/review', ReviewView.as_view())
]