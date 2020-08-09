from basketapp.models import Basket


def basket(request):
    user_basket = Basket.objects.filter(user=request.user) if request.user.is_authenticated else []
    return {
        'basket': user_basket
    }
