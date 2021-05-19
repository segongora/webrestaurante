from django.contrib import admin
from .models import Salsa


# Register your models here.

class SalsaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    # Columas que se quieren mostrar
    list_display = ('name', 'updated')
    ordering = ('name',)
    search_fields = ('name', )

admin.site.register(Salsa, SalsaAdmin)