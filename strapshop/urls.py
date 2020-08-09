"""strapshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import re_path
from django.conf.urls import include

from mainapp.views import (
    main, about_us
)
# Replace to include function this import
from authapp.views import (
    logout, login, edit, register,
    verify
)


urlpatterns = [
    # Home
    re_path(r'^$', main, name='home'),
    # Contacts
    re_path(r'^about_us/$', about_us, name='about_us'),
    # Products
    re_path(r'^strap/', include('mainapp.urls', namespace='strap')),
    # Auth
    re_path(r'^login/$', login, name='login'),
    re_path(r'^logout/$', logout, name='logout'),
    re_path(r'^edit/$', edit, name='edit'),
    re_path(r'^register/$', register,  name='register'),
    re_path(r'^verify/(?P<email>.+)/(?P<activation_key>\w+)/$', verify, name='verify'),
    # Basket
    re_path(r'^basket/', include('basketapp.urls', namespace='basket')),
    # Admin
    re_path(r'^admin/', include('adminapp.urls', namespace='admin')),
]

# Not in production
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
