from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse

from adminapp.forms import StrapUserAdminChangeForm, ProductAdminChangeForm
from authapp.forms import StrapUserRegisterForm
from authapp.models import StrapUser
from mainapp.models import Product


# Users controllers
@user_passes_test(lambda user: user.is_superuser)
def users(request):
    title = 'админка/список полльзователей'
    ordered_list = ['-is_active', '-is_superuser', 'username']
    users_list = StrapUser.objects.all().order_by(*ordered_list)

    content = {
        'title': title,
        'users': users_list
    }
    return render(
        request,
        'adminapp/users.html',
        context=content
    )


@user_passes_test(lambda user: user.is_superuser)
def user_create(request):
    title = 'админка/cоздать пользователя'

    if request.method == 'POST':
        user_create_form = StrapUserRegisterForm(request.POST)
        if user_create_form.is_valid():
            user_create_form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        user_create_form = StrapUserRegisterForm()

    content = {
        'title': title,
        'user_form': user_create_form
    }
    return render(
        request,
        'adminapp/user_update.html',
        context=content
    )


@user_passes_test(lambda user: user.is_superuser)
def user_update(request, pk):
    title = 'админка/редактировать полльзователя'

    update_user = get_object_or_404(StrapUser, pk=pk)
    if request.method == 'POST':
        user_update_form = StrapUserAdminChangeForm(request.POST, instance=update_user)
        if user_update_form.is_valid():
            user_update_form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        user_update_form = StrapUserAdminChangeForm(instance=update_user)

    content = {
        'title': title,
        'user_form': user_update_form
    }
    return render(
        request,
        'adminapp/user_update.html',
        context=content
    )


@user_passes_test(lambda user: user.is_superuser)
def user_delete(request, pk):
    user_to_delete = get_object_or_404(StrapUser, pk=pk)
    user_to_delete.is_active = False
    user_to_delete.save()
    return HttpResponseRedirect(reverse('admin:users'))


# Products controllers
@user_passes_test(lambda user: user.is_superuser)
def products(request):
    title = 'админка/список продуктов'
    ordered_list = ['name']
    products_list = Product.objects.all().order_by(*ordered_list)

    content = {
        'title': title,
        'products': products_list
    }
    return render(
        request,
        'adminapp/products.html',
        context=content
    )


@user_passes_test(lambda user: user.is_superuser)
def product_create(request):
    title = 'админка/создать продукт'

    if request.method == 'POST':
        product_create_form = ProductAdminChangeForm(request.POST, request.FILES)
        if product_create_form.is_valid():
            product_create_form.save()
            return HttpResponseRedirect(reverse('admin:products'))
    else:
        product_create_form = ProductAdminChangeForm()

    content = {
        'title': title,
        'product_form': product_create_form
    }
    return render(
        request,
        'adminapp/product_update.html',
        context=content
    )


@user_passes_test(lambda user: user.is_superuser)
def product_page(request, pk):
    return HttpResponseRedirect(reverse('strap:product_id', args=[pk]))


@user_passes_test(lambda user: user.is_superuser)
def product_update(request, pk):
    title = 'админка/редактировать продукт'

    product_to_update = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product_update_form = ProductAdminChangeForm(request.POST, request.FILES, instance=product_to_update)
        if product_update_form.is_valid():
            product_update_form.save()
            return HttpResponseRedirect(reverse('admin:products'))
    else:
        product_update_form = ProductAdminChangeForm(instance=product_to_update)

    content = {
        'title': title,
        'product_form': product_update_form
    }
    return render(
        request,
        'adminapp/product_update.html',
        context=content
    )


@user_passes_test(lambda user: user.is_superuser)
def product_delete(request, pk):
    product_to_delete = get_object_or_404(Product, pk=pk)
    product_to_delete.is_active = False
    product_to_delete.save()
    return HttpResponseRedirect(reverse('admin:products'))
