// =============================================
// HES ATACADO — Home (destaques + funções gerais)
// =============================================

// Ano automático no rodapé
const ano = document.getElementById('ano');
if (ano) ano.textContent = new Date().getFullYear();

// Carrega os produtos em destaque na home
async function carregarDestaques() {
    const container = document.getElementById('produtosDestaque');
    if (!container) return;

    container.innerHTML = '<p class="sem-imagem" style="grid-column:1/-1;">Carregando produtos...</p>';

    const produtos = await buscarProdutos('', '', true);

    if (!produtos.length) {
        container.innerHTML = '<p class="sem-imagem" style="grid-column:1/-1;">Nenhum produto em destaque ainda. Marque "Destaque na home" no painel.</p>';
        return;
    }

    container.innerHTML = produtos.map(criarCardProduto).join('');
}

// Inicia ao carregar a página
document.addEventListener('DOMContentLoaded', carregarDestaques);