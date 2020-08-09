from django.urls import re_path

from basketapp.views import (
    view, add, remove
)

app_name = 'basketapp'

urlpatterns = [
    re_path(r'^$', view, name='view'),
    re_path(r'^add/(?P<pk>\d+)/$', add, name='add'),
    re_path(r'^remove/(?P<pk>\d+)/$', remove, name='remove')
]
