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


class ProductDetailView(DetailView):
    model = Product
