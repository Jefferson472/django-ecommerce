from django.views.generic.edit import FormView
from django.shortcuts import render

from apps.cart.cart import Cart
from .forms import OrderCreateForm
from .models import OrderItem
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
            return render(
                request, 'orders/created.html', {'order': order}
            )

        return super().post(request, *args, **kwargs)
