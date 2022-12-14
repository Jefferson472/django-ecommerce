from django.urls import path

from .views import ProductListView, ProductDetailView


urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('product-category/<slug:slug>', ProductListView.as_view(), name='product_list_by_category'),
    path('product/<int:pk>/<slug:slug>', ProductDetailView.as_view(), name='product_detail'),
]
