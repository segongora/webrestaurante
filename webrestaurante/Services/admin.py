from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    # campos de lectura
    readonly_fields = ('created', 'updated')


admin.site.register(Service, ServiceAdmin)

# Register your models here.
