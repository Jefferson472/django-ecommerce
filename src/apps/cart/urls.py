from django.urls import path

from .views import CartDetailView, cart_add, cart_remove


urlpatterns = [
    path('', CartDetailView.as_view(), name='cart_detail'),
    path('add/<int:product_id>', cart_add, name='cart_add'),
    path('remove/<int:product_id>', cart_remove, name='cart_remove'),
]
