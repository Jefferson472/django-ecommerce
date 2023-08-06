from django.urls import path
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

from .views import ProductListView, ProductDetailView


urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path(_('product-category/<slug:slug>'), ProductListView.as_view(), name='product_list_by_category'),
    path(_('product/<int:pk>/<slug:slug>'), ProductDetailView.as_view(), name='product_detail'),
]
