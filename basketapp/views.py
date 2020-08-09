from django.shortcuts import (
    render,
    get_object_or_404,
    HttpResponseRedirect
)
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from mainapp.models import Product
from basketapp.models import Basket


@login_required
def view(request):
    title = 'корзина'
    user_basket = Basket.objects.filter(user=request.user)

    content = {
        'title': title,
        'basket': user_basket
    }
    return render(request, 'basketapp/basket.html', context=content)


@login_required
def add(request, pk):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('strap:product_id', args=[pk]))

    product = get_object_or_404(Product, pk=pk)
    user_basket = Basket.objects.filter(user=request.user, product=product).first()
    if not user_basket:
        user_basket = Basket(user=request.user, product=product)

    user_basket.quantity += 1
    user_basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def remove(request, pk):
    product = get_object_or_404(Basket, pk=pk)
    product.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
