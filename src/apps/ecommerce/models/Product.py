from django.db import models
from django.urls import reverse

from parler.models import TranslatableModel, TranslatedFields

from .Category import Category


class Product(TranslatableModel):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    translations = TranslatedFields(description = models.TextField(blank=True))
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_product'

        # as pequisas serão feitas por id e slug e isso melhora o desempenho
        # index_together = (('id', 'slug'),) # o tradutor parler não oferecer suporte ao index_together
        
        # ordering = ('name',) # o tradutor parler não oferecer suporte ao ordering
        verbose_name = ('Produto')
        verbose_name_plural = ('Produtos')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'pk': self.pk, 'slug': self.slug})
