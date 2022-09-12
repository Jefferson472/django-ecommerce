from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic.edit import FormView

from apps.ecommerce.models import Product
from .cart import Cart
from .forms import CartAddProductForm


class CartDetailView(FormView):
    form_class  = CartAddProductForm
    template_name = "cart/cart_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart(self.request)
        for item in cart:
            item['update_quantity_form'] = CartAddProductForm(
                initial={'quantity': item['quantity'], 'override': True}
            )
        context['cart'] = cart
        return context


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            product=product,
            quantity=cd['quantity'],
            override_quantity=cd['override']
        )
    return redirect('cart_detail')

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')
