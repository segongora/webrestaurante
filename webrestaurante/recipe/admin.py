from django.contrib import admin
from .models import Recipe, Pedido

class PedidoAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha',)
    # Columas que se quieren mostrar
    list_display = ('fecha', 'nombre', 'total')
    ordering = ('fecha',)
    search_fields = ('nombre', )


class RecipeAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    # Columas que se quieren mostrar
    list_display = ('title', 'updated')
    ordering = ('title',)
    search_fields = ('title', )

admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Recipe, RecipeAdmin)
