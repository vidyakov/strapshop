from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Product


def get_same_products(current_product_pk: int):
    return Product.objects.exclude(pk=current_product_pk)[:3]


def main(request):
    products_left = Product.objects.filter(is_active=True)[:2]
    products_right = Product.objects.filter(is_active=True)[2:]

    content = {
        'title': 'ремешки Salik',
        'products': zip(products_right, products_left),
    }

    return render(
        request,
        'mainapp/home.html',
        context=content
    )


def output(request, pk: int = 1, page=1):
    strap = get_object_or_404(Product, pk=pk)
    title = 'ремешок для ' + strap.name
    same_products = get_same_products(pk)

    # For image pagination
    photos = [strap.image1, strap.image2, strap.image3]
    paginator = Paginator(photos, 1)
    try:
        main_photo = paginator.page(page)
    except PageNotAnInteger:
        main_photo = paginator.page(1)
    except EmptyPage:
        main_photo = paginator.page(paginator.num_pages)

    content = {
        'title': title,
        'product': strap,
        'same': same_products,
        'main_photo': main_photo
    }
    return render(
        request,
        'mainapp/output.html',
        context=content
    )


def about_us(request):
    text = """Твой самый лучший на свете текст для этого сайта. Твой самый лучший на свете текст для этого сайта. Твой самый лучший на свете текст для этого сайта. Твой самый лучший на свете текст для этого сайта. Твой самый лучший на свете текст для этого сайта. Твой самый лучший на свете текст для этого сайта. 
    Твой самый лучший на свете текст для этого сайта. Твой самый лучший на свете текст для этого сайта. 
    Твой самый лучший на свете текст для этого сайта. Твой самый лучший на свете текст для этого сайта. Твой самый лучший на свете текст для этого сайта. Твой самый лучший на свете текст для этого сайта. Твой самый лучший на свете текст для этого сайта. Твой самый лучший на свете текст для этого сайта. 
    Твой самый лучший на свете текст для этого сайта. Твой самый лучший на свете текст для этого сайта. 
    """

    content = {
        'title': 'Про нас',
        'text': text,
        'headline': 'Лучшие браслетики',
        'minititle': 'Настя',
        'bigtitle': 'Допиши',
    }
    return render(
        request,
        'mainapp/about_us.html',
        context=content
    )
