from django.db import models
from django.conf import settings
from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='basket'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(
        verbose_name='Количество',
        default=0
    )
    time = models.DateTimeField(
        verbose_name='Время',
        auto_now_add=True
    )

    @property
    def product_cost(self):
        return self.product.price * self.quantity

    @property
    def total_quantity(self):
        _items = Basket.objects.filter(user=self.user)
        return sum(map(lambda x: x.quantity, _items))

    @property
    def total_cost(self):
        _items = Basket.objects.filter(user=self.user)
        return sum(map(lambda x: self.product_cost, _items))

    def __str__(self):
        return f'{self.user} {self.total_quantity}'
