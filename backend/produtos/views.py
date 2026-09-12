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

    if not categoria_id and not busca and not destaque:
        produtos = produtos[:24]

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
            'destaque': p.destaque,   # <-- ADICIONADO
        })
    return JsonResponse(dados, safe=False)