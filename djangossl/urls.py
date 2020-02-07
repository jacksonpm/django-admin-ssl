from django.urls import path

from djangossl.views import ssl_http

urlpatterns = [
    path(r'.well-known/acme-challenge/<chave>', ssl_http),
]
