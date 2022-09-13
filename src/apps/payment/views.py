import braintree
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings

from apps.orders.models import Order


# instancia o gateway de pagamento da Braintree
gateway = braintree.BraintreeGateway(settings.BRAINTREE_CONF)

def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    total_cost = order.get_total_cost()

    if request.method == 'POST':
        nonce = request.POST.get('payment_method_nonce', None) # obtém o nonce
        # cria e submete a transação
        result = gateway.transaction.sale({
            'amount': f'{total_cost:.2f}',
            'payment_method_nonce': nonce,
            'options': {
                'submit_for_settlement': True
            }
        })
    
        if result.is_success:
            order.paid = True # marca o status da instância Order como pago
            order.braintree_id = result.transaction.id # armazena o id de transação único
            order.save()
            return redirect('payment:done')
        else:
            return redirect('payment:canceled')
    else:
        client_token = gateway.client_token.generate() # gerar o token
        return render(
            request, 'payment/process.html',
            {'order': order, 'client_token': client_token}
        )

def payment_done(request):
    return render(request, 'payment/done.html')

def payment_canceled(request):
    return render(request, 'payment/canceled.html')
