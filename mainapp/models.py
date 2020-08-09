from django.db import models as md


class Product(md.Model):
    name = md.CharField(
        verbose_name='Имя продукта (Ремешок для)',
        max_length=128
    )
    image_on_home = md.ImageField(
        verbose_name='Фото на главной странице',
        upload_to='products_images',
        blank=True
    )
    image1 = md.ImageField(
        verbose_name='Product photo number 1',
        upload_to='products_images',
        blank=True
    )
    image2 = md.ImageField(
        verbose_name='Product photo number 2',
        upload_to='products_images',
        blank=True,
    )
    image3 = md.ImageField(
        verbose_name='Product photo number 3',
        upload_to='products_images',
        blank=True
    )
    description = md.CharField(
        max_length=600,
        verbose_name='Описание продукта',
        blank=True
    )
    short_description = md.CharField(
        max_length=300,
        verbose_name='Краткое описание',
        blank=True
    )
    price = md.DecimalField(
        verbose_name='Цена',
        default=0,
        decimal_places=2,
        max_digits=8
    )

    is_active = md.BooleanField(
        verbose_name='Активенин или нет',
        default=True,
    )

    def __str__(self):
        return f'{self.name} {self.price}'
