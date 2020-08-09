from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from django.core.mail import send_mail
from django.conf import settings

from authapp.models import StrapUser
from authapp.forms import (
    StrapUserLoginForm, StrapUserRegisterForm,
    StrapUserChangeForm
)


def send_verify_mail(user):
    verify_link = reverse('verify', args=[user.email, user.activation_key])

    title = f'Подтверждение учетной записи {user.username}'
    message = f'Для подтверждения перейдите по ссылке: {settings.DOMAIN_NAME}{verify_link}'

    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


def verify(request, email, activation_key):
    try:
        user = StrapUser.objects.get(email=email)
        if user.activation_key == activation_key and user.is_activation_key_expired:
            user.is_active = True
            user.save()
            auth.login(request, user)
            return render(request, 'authapp/verify.html')
    except Exception as e:
        print(e, e.args)
        return HttpResponseRedirect(reverse('home'))


def login(request):
    title = 'вход'
    next_url = request.GET['next_url'] if 'next_url' in request.GET.keys() else ''
    login_form = StrapUserLoginForm(data=request.POST)

    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(
            username=username,
            password=password
        )
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('home'))

    content = {
        'title': title,
        'login_form': login_form,
        'next_url': next_url
    }
    return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('home'))


def edit(request):
    title = 'редактирование'

    if request.method == 'POST':
        edit_form = StrapUserChangeForm(
            request.POST,
            request.FILES,
            instance=request.user
        )
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('edit'))
    else:
        edit_form = StrapUserChangeForm(instance=request.user)

    content = {
        'title': title,
        'edit_form': edit_form
    }
    return render(request, 'authapp/edit.html', content)


def register(request):
    title = 'регистрация'

    if request.method == 'POST':
        register_form = StrapUserRegisterForm(request.POST, request.FILES)  # .FILES for media files
        if register_form.is_valid():
            user = register_form.save()
            if send_verify_mail(user):
                return HttpResponseRedirect(reverse('login'))
            return HttpResponseRedirect(reverse('home'))
    else:
        register_form = StrapUserRegisterForm()

    content = {
        'title': title,
        'register_form': register_form
    }
    return render(request, 'authapp/register.html', content)
