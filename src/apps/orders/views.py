import weasyprint

from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic.edit import FormView

from apps.cart.cart import Cart
from .forms import OrderCreateForm
from .models import OrderItem, Order
from .tasks import order_created


class OrderFormView(FormView):
    form_class  = OrderCreateForm
    success_url  = 'orders/created'
    template_name = 'orders/create.html'

    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear() # limpa o carrinho

            order_created.delay(order.id) # dispara uma tarefa assíncrona
            request.session['order_id'] = order.id # define o pedido na sessão
            return redirect(reverse('payment:process'))

        return super().post(request, *args, **kwargs)


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(
        request,
        'admin/orders/order/detail.html',
        {'order': order},
    )


@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('orders/pdf.html', {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
    weasyprint.HTML(string=html).write_pdf(
        response, stylesheets=[weasyprint.CSS(
            settings.STATIC_ROOT + 'css/pdf.css'
        )]
    )
    return response
