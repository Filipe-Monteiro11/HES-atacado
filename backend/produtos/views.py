from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count, Q
from .models import Categoria, Produto

def home(request):
    return render(request, 'home.html')

def produtos(request):
    return render(request, 'produtos.html')

# =============================================
# API para o frontend (api.js consome estes dados)
# =============================================

def api_categorias(request):
    categorias = (
        Categoria.objects.filter(ativo=True)
        .annotate(
            qtd=Count(
                'subcategorias__produtos',
                filter=Q(subcategorias__produtos__ativo=True),
                distinct=True,
            )
        )
        .order_by('ordem', 'nome')
    )
    dados = [{'id': c.id, 'nome': c.nome, 'qtd': c.qtd} for c in categorias]
    return JsonResponse(dados, safe=False)

def api_produtos(request):
    produtos = (
        Produto.objects.filter(ativo=True)
        .select_related('subcategoria__categoria')
        .order_by('subcategoria__categoria__ordem', 'subcategoria__ordem', 'nome')
    )

    categoria_id = request.GET.get('categoria')
    busca = request.GET.get('busca', '').strip()
    destaque = request.GET.get('destaque', '').strip()

    if categoria_id:
        produtos = produtos.filter(subcategoria__categoria_id=categoria_id)

    if busca:
        produtos = produtos.filter(
            Q(nome__icontains=busca) | Q(codigo__icontains=busca)
        )

    if destaque == '1':
        produtos = produtos.filter(destaque=True)

    # CORTE REMOVIDO: antes existia "produtos = produtos[:24]" aqui,
    # que limitava a listagem geral a 24 produtos.
    # Agora o catálogo completo (193 produtos) é exibido em "Todos os Produtos".

    dados = []
    for p in produtos:
        dados.append({
            'id': p.id,
            'nome': p.nome,
            'codigo': p.codigo,
            'descricao': getattr(p, 'descricao', '') or '',
            'imagem': p.imagem.url if p.imagem else None,
            'categoria_id': p.subcategoria.categoria_id,
            'categoria': f"{p.subcategoria.categoria.nome} — {p.subcategoria.nome}",
            'destaque': p.destaque,
        })
    return JsonResponse(dados, safe=False)