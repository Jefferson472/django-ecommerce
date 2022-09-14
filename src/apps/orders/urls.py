from django.urls import path

from .views import OrderFormView, admin_order_detail


app_name = 'orders'

urlpatterns = [
    path('create/', OrderFormView.as_view(), name='order_create'),
    path('admin/order/<int:order_id>/', admin_order_detail, name='admin_order_detail'),
]
