from django.urls import path
from django.utils.translation import gettext_lazy as _

from .views import OrderFormView, admin_order_detail, admin_order_pdf


app_name = 'orders'

urlpatterns = [
    path(_('create/'), OrderFormView.as_view(), name='order_create'),
    path('admin/order/<int:order_id>/', admin_order_detail, name='admin_order_detail'),
    path('admin/order/<int:order_id>/pdf/', admin_order_pdf, name='admin_order_pdf'),
]
