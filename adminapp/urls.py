from django.urls import re_path

import adminapp.views as adminapp


app_name = 'adminapp'

urlpatterns = [
    # Products paths
    re_path(r'^$', adminapp.products),
    re_path(r'^product/create/$', adminapp.product_create, name='product_create'),
    re_path(r'^products/$', adminapp.products, name='products'),
    re_path(r'^product/page/(?P<pk>\d+)/$', adminapp.product_page, name='page'),
    re_path(r'^product/update/(?P<pk>\d+)/$', adminapp.product_update, name='product_update'),
    re_path(r'^product/delete/(?P<pk>\d+)/$', adminapp.product_delete, name='product_delete'),

    # Users paths
    re_path(r'^user/create/$', adminapp.user_create, name='user_create'),
    re_path(r'^users/$', adminapp.users, name='users'),
    re_path(r'^user/update/(?P<pk>\d+)/$', adminapp.user_update, name='user_update'),
    re_path(r'^user/delete/(?P<pk>\d+)/$', adminapp.user_delete, name='user_delete'),

]
