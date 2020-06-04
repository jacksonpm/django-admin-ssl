from django.http import HttpResponse
from djangossl.models import SSL

def ssl_http(request, chave):
    ssl = SSL.objects.filter(chave=chave)
    if ssl:
        valor = str(ssl[0].valor)
        valor = '\n\r'.join(valor.split())
    else:
        valor = ''
    return HttpResponse(valor)
