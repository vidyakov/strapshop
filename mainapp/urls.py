from django.urls import re_path

import mainapp.views as mainapp


app_name = 'mainapp'

urlpatterns = [
    re_path(r'^(?P<pk>\d+)/$', mainapp.output, name='product_id'),
    re_path(r'^(?P<pk>\d+)/page/(?P<page>\d+)/$', mainapp.output, name='page'),
]
