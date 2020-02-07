from django.contrib import admin

from djangossl.models import SSL


@admin.register(SSL)
class AdminSSL(admin.ModelAdmin):

    def has_module_permission(self, request):
        return request.user.is_superuser