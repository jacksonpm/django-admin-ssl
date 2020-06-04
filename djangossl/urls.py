from django.urls import path

from djangossl.views import ssl_http

urlpatterns = [
    path(r'.well-known/pki-validation/<chave>.txt', ssl_http),
]
