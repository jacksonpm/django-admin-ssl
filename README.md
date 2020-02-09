Include django-admin-ssl in urls:

```python
from djangossl import urls as ssl_urls

urlpatterns = [
    ...
    url('', include(ssl_urls)),
]
```

Include in INSTALLED_APPS

```python
INSTALLED_APPS = [
    ...,
    'djangossl',
]
```
