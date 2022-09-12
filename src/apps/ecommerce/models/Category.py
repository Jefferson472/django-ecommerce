from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)    

    class Meta:
        db_table = 'tb_category'
        ordering = ('name',)
        verbose_name = ('Categoria')
        verbose_name_plural = ('Categorias')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list_by_category', kwargs={'slug': self.slug})
