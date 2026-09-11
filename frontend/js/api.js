// =============================================
// HES ATACADO — API (busca os dados do backend Django)
// Os produtos e categorias vêm do seu painel admin.
// =============================================

const API_BASE = '/api';

// Busca as categorias com quantidade de produtos
async function buscarCategorias() {
    try {
        const resposta = await fetch(`${API_BASE}/categorias/`);
        if (!resposta.ok) throw new Error('Falha ao buscar categorias');
        return await resposta.json();
    } catch (erro) {
        console.error('Erro ao carregar categorias:', erro);
        return [];
    }
}

// Busca os produtos (filtra por categoria, busca ou destaque)
async function buscarProdutos(categoriaId = '', busca = '', destaque = false) {
    try {
        let url = `${API_BASE}/produtos/`;
        const params = new URLSearchParams();
        if (categoriaId) params.append('categoria', categoriaId);
        if (busca) params.append('busca', busca);
        if (destaque) params.append('destaque', '1');
        if (params.toString()) url += `?${params.toString()}`;

        const resposta = await fetch(url);
        if (!resposta.ok) throw new Error('Falha ao buscar produtos');
        return await resposta.json();
    } catch (erro) {
        console.error('Erro ao carregar produtos:', erro);
        return [];
    }
}

// Cria o HTML do card de um produto
function criarCardProduto(produto) {
    const imagem = produto.imagem
        ? `<img src="${produto.imagem}" alt="${produto.nome}" loading="lazy">`
        : `<span class="sem-imagem">${produto.codigo}</span>`;

    const categoriaNome = produto.categoria || 'Produto';

    return `
        <div class="produto-card" data-categoria="${produto.categoria_id || ''}">
            <div class="img-wrapper">${imagem}</div>
            <div class="produto-info">
                <span class="categoria-tag">${categoriaNome}</span>
                <h3>${produto.nome}</h3>
                ${produto.descricao ? `<p>${produto.descricao}</p>` : ''}
            </div>
        </div>
    `;
}