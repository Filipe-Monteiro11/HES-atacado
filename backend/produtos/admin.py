from django.contrib import admin
from django.utils.html import format_html
from .models import Categoria, Subcategoria, Produto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'ordem', 'ativo')
    list_filter = ('ativo',)
    search_fields = ('nome', 'descricao')
    list_editable = ('ordem', 'ativo')

@admin.register(Subcategoria)
class SubcategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'ordem', 'ativo')
    list_filter = ('categoria', 'ativo')
    search_fields = ('nome', 'descricao')
    list_editable = ('ordem', 'ativo')
    list_select_related = ('categoria',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'subcategoria', 'destaque', 'ativo')
    list_filter = ('ativo', 'destaque')
    search_fields = ('codigo', 'nome', 'descricao')
    list_editable = ('destaque', 'ativo')
    list_select_related = ('subcategoria__categoria',)
    autocomplete_fields = ('subcategoria',)
    readonly_fields = ('imagem_preview',)
    list_per_page = 20

    fieldsets = (
        ('Informações Básicas', {
            'fields': ('subcategoria', 'codigo', 'nome', 'descricao'),
        }),
        ('Imagem do Produto', {
            'fields': ('imagem', 'imagem_preview'),
            'description': 'Clique em "Escolher arquivo" para enviar a foto do produto.',
        }),
        ('Status', {
            'fields': ('destaque', 'ativo'),
        }),
    )

    def imagem_preview(self, obj):
        if obj.imagem:
            return format_html(
                '<img src="{}" style="max-width:220px;border-radius:8px;box-shadow:0 2px 6px rgba(0,0,0,.2);" />',
                obj.imagem.url
            )
        return 'Nenhuma imagem enviada ainda.'

    imagem_preview.short_description = 'Prévia da imagem'