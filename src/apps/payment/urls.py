from django.urls import path
from django.utils.translation import gettext_lazy as _

from .views import payment_canceled, payment_done, payment_process


app_name = 'payment'

urlpatterns = [
    path(_('process/'), payment_process, name='process'),
    path(_('done/'), payment_done, name='done'),
    path(_('canceled/'), payment_canceled, name='canceled'),
]
