from unicodedata import category
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Category, Product


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
            context['category'] = get_object_or_404(Category, slug=kwargs['category_slug'])
        return context


class ProductDetailView(DetailView):
    model = Product
