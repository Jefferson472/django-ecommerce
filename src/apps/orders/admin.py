from django.contrib import admin

from .models import Order, OrderItem
from .utils.admin_order import order_detail, order_pdf
from .utils.csv import export_csv


order_pdf.short_description = 'Invoice'

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'first_name', 'last_name', 'email',
        'address', 'postal_code', 'city', 'paid',
        'created', 'updated', order_detail, order_pdf
    ]
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
    actions = [export_csv]
