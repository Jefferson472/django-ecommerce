from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
    """Tarefa para enviar uma notificação por email quando um pedido for criado com sucesso"""
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name}, \n\n' \
                f'You have successfully placed an order.' \
                f'Your order ID is {order.id}'

    return send_mail(
        subject, message, 'admin@django-ecommerce.com', [order.email],
    )
