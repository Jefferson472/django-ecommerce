from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.utils.translation import gettext_lazy as _


urlpatterns = i18n_patterns(
    path(_("admin/"), admin.site.urls),
    path(_('cart/'), include('apps.cart.urls')),
    path(_('orders/'), include('apps.orders.urls')),
    path(_('payment/'), include('apps.payment.urls')),
    path(_('coupons/'), include('apps.coupons.urls')),
    path(_('rosetta/'), include('rosetta.urls')),
    path('', include('apps.ecommerce.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
