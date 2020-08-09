from django.urls import re_path

import authapp.views as authapp


app_name = 'authapp'

url_patterns = [
    # re_path(r'^login/$', authapp.login, name='login'),
    # re_path(r'logout/', authapp.logout, name='logout')
]
