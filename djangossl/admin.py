from django.contrib import admin
from django.db.models import CharField
from django.forms import Textarea

from djangossl.models import SSL

@admin.register(SSL)
class AdminSSL(admin.ModelAdmin):
    formfield_overrides = {
        CharField: {'widget': Textarea(attrs={'rows': 2, 'cols': 80, 'style': 'font-size: 15px;'})},
    }
    def has_module_permission(self, request):
        return request.user.is_superuser
