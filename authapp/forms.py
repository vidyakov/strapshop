import hashlib, random

from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm, UserCreationForm,
    UserChangeForm
)

from .models import StrapUser


class StrapUserLoginForm(AuthenticationForm):
    class Meta:
        model = StrapUser
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(StrapUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class StrapUserRegisterForm(UserCreationForm):
    class Meta:
        model = StrapUser
        fields = (
            'username', 'email', 'password1', 'password2',
            'first_name', 'age'
        )

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def clean_age(self):
        user_age = self.cleaned_data['age']
        print(user_age, type(user_age))
        if user_age < 18:
            raise forms.ValidationError('Ваш возраст слишком мал')

        return user_age

    def save(self):
        user = super(StrapUserRegisterForm, self).save()
        user.is_active = False

        salt = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:6]
        user.activation_key = hashlib.sha1((user.email + salt).encode('utf-8')).hexdigest()[:6]

        user.save()
        return user


class StrapUserChangeForm(UserChangeForm):
    class Meta:
        model = StrapUser
        fields = (
            'username', 'email',
            'password'
        )

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

            if field_name == 'password':
                field.widget = forms.HiddenInput()

    def clean_age(self):
        user_age = self.cleaned_data['age']
        if user_age < 18:
            raise forms.ValidationError('Опять тренирую эту хуету')

        return user_age
