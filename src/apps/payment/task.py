import weasyprint
from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from io import BytesIO

from apps.orders.models import Order


@shared_task
def payment_completed(order_id):
    """Tarefa para enviar uma notificação por email quando um pedido é criado com sucesso"""
    order = Order.objects.get(id=order_id)

    # cria o email
    subject = f'Django Ecommerce - EE Invoice no. {order.id}'
    message = 'Please, find attached the invoice for your recet puchase.'
    email = EmailMessage(
        subject, message, 'admin@django-ecommerce.com', [order.email]
    )

    # gera o PDF
    html = render_to_string('orders/pdf.html', {'order': order})
    out = BytesIO()
    stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)

    # anexa o PDF
    email.attach(f'order_{order.id}.pdf', out.getvalue(), 'application/pdf')

    # envia o email
    email.send()
