// =============================================
// HES ATACADO — Página de Produtos
// Categoria na sidebar → mostra os produtos dela
// =============================================

// Ano automático no rodapé
const ano = document.getElementById('ano');
if (ano) ano.textContent = new Date().getFullYear();

// Carrega as categorias na sidebar
async function carregarCategorias() {
    const container = document.getElementById('listaCategorias');
    if (!container) return;

    const categorias = await buscarCategorias();

    container.innerHTML = categorias.map(cat => `
        <button class="categoria-btn" data-categoria="${cat.id}" data-nome="${cat.nome}">
            <span class="cat-nome">${cat.nome}</span>
            <span class="cat-qtd">${cat.qtd}</span>
        </button>
    `).join('');

    container.querySelectorAll('.categoria-btn').forEach(btn => {
        btn.addEventListener('click', () => selecionarCategoria(btn));
    });
}

// Aplica o clique no botão "Todos os produtos" (já existe no HTML)
const botaoTodos = document.querySelector('.categoria-btn.active');
if (botaoTodos) {
    botaoTodos.addEventListener('click', () => selecionarCategoria(botaoTodos));
}

// Seleciona uma categoria e carrega os produtos dela
async function selecionarCategoria(botao) {
    document.querySelectorAll('.categoria-btn').forEach(b => b.classList.remove('active'));
    botao.classList.add('active');

    const categoriaId = botao.dataset.categoria;
    const nome = botao.dataset.nome || 'Todos os Produtos';
    document.getElementById('tituloCategoria').textContent = nome;

    const container = document.getElementById('produtosGrid');
    if (!container) return;

    container.innerHTML = '<p class="mensagem-vazia">Carregando produtos...</p>';

    const produtos = await buscarProdutos(categoriaId);

    const contador = document.getElementById('contadorProdutos');
    if (contador) contador.textContent = produtos.length ? `${produtos.length} produto${produtos.length !== 1 ? 's' : ''}` : '';

    if (!produtos.length) {
        container.innerHTML = '<p class="mensagem-vazia">Nenhum produto encontrado nesta categoria.</p>';
        return;
    }

    container.innerHTML = produtos.map(criarCardProduto).join('');
}

// Inicia ao carregar a página
document.addEventListener('DOMContentLoaded', () => {
    carregarCategorias();
    // Carrega os produtos da primeira seleção (Todos)
    const ativo = document.querySelector('.categoria-btn.active');
    if (ativo) selecionarCategoria(ativo);
});