from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)] # os validadores são usados para garantir limites entre 0 e 100
    )
    active = models.BooleanField()

    class Meta:
        db_table = 'tb_coupons'
        ordering = ('-valid_to',)
        verbose_name = ('Coupon')
        verbose_name_plural = ('Coupons')

    def __str__(self):
        return self.code
