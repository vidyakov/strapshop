from django import template
from django.conf import settings


REGISTER = template.Library()


@REGISTER.filter(name='media_folder_products')
def media_folder_products(string):
    return f'{settings.MEDIA_URL}{string}'


@REGISTER.filter(name='media_folder_users')
def media_folder_users(string):
    return f'{settings.MEDIA_URL}{string}'
