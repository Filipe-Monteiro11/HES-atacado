from django.contrib import admin
from django.utils.html import format_html
from .models import Categoria, Subcategoria, Produto

class CategoriaFilter(admin.SimpleListFilter):
    """Filtro para escolher a categoria e ver todos os produtos dela."""
    title = 'Categoria'
    parameter_name = 'categoria'

    def lookups(self, request, model_admin):
        # Mostra só as categorias ativas (são poucas, então é leve)
        categorias = Categoria.objects.filter(ativo=True).order_by('ordem', 'nome')
        return [(c.id, c.nome) for c in categorias]

    def queryset(self, request, queryset):
        # Ao escolher uma categoria, retorna todos os produtos dela
        if self.value():
            return queryset.filter(subcategoria__categoria_id=self.value())
        return queryset

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
    list_filter = (CategoriaFilter, 'ativo', 'destaque')
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