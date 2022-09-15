from itertools import product
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

from .models import Category, Product
from .recommender import Recommender
from apps.cart.forms import CartAddProductForm


class ProductListView(ListView):
    model = Product
    queryset = Product.objects.filter(available=True)

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset()
        if kwargs.get('category_slug'):
            queryset = queryset.filter(category=kwargs['category_slug'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()

        if kwargs.get('category_slug'):
            language = self.request.LANGUAGE_CODE
            context['category'] = get_object_or_404(
                Category,
                translations__language_code=language,
                translations__slug=kwargs['category_slug'],
            )

        return context


class ProductDetailView(DetailView, FormView):
    model = Product
    form_class  = CartAddProductForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        r = Recommender()
        product = self.object
        context['recommended_products'] = r.suggest_products_for([product], 4)

        return context