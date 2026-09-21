// =============================================
// HES ATACADO — Página de Produtos
// Categoria na sidebar → mostra os produtos dela
// =============================================

// Ano automático no rodapé
const ano = document.getElementById('ano');
if (ano) ano.textContent = new Date().getFullYear();

// ---------------------------------------------
// FOTO DE FUNDO AUTOMÁTICA POR CATEGORIA
// O nome do arquivo é o nome da categoria "limpo":
//   minúsculas, sem acento, e tudo que não é letra/número vira "-"
//   Ex.: "Laticínios"                 -> laticinios.png
//        "Dispensers — Linha Gold"    -> dispensers-linha-gold.png
// Basta colocar a imagem em static/img/ com esse nome.
// Se não existir imagem pra categoria, fica o visual padrão.
// ---------------------------------------------
const PASTA_BANNERS = '/static/img/';
const EXTENSOES = ['png', 'jpg', 'jpeg', 'webp'];   // formatos aceitos
const cacheFundos = {};
let categoriaAtual = '';

function normalizar(texto) {
    return (texto || '')
        .normalize('NFD')
        .replace(/[\u0300-\u036f]/g, '')
        .toLowerCase()
        .trim();
}

function gerarSlug(texto) {
    return normalizar(texto).replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '');
}

function testarImagem(url) {
    return new Promise(resolve => {
        const img = new Image();
        img.onload = () => resolve(true);
        img.onerror = () => resolve(false);
        img.src = url;
    });
}

async function descobrirFundo(nomeCategoria) {
    const slug = gerarSlug(nomeCategoria);
    if (!slug) return null;
    if (slug in cacheFundos) return cacheFundos[slug];

    for (const ext of EXTENSOES) {
        const url = `${PASTA_BANNERS}${slug}.${ext}`;
        if (await testarImagem(url)) {
            cacheFundos[slug] = url;
            return url;
        }
    }
    cacheFundos[slug] = null;
    return null;
}

async function atualizarBanner(nomeCategoria) {
    const url = await descobrirFundo(nomeCategoria);

    // se o usuário já clicou em outra categoria enquanto carregava, ignora
    if (nomeCategoria !== categoriaAtual) return;

    if (url) {
        document.body.style.setProperty('--foto-fundo', `url('${url}')`);
        document.body.classList.add('com-foto');
    } else {
        document.body.style.removeProperty('--foto-fundo');
        document.body.classList.remove('com-foto');
    }
}

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

    // Troca a foto do banner conforme a categoria
    categoriaAtual = nome;
    atualizarBanner(nome);

    const container = document.getElementById('produtosGrid');
    if (!container) return;

    container.innerHTML = '<p class="mensagem-vazia">Carregando produtos...</p>';

    const produtos = await buscarProdutos(categoriaId);

    const contador = document.getElementById('contadorProdutos');
    if (contador) contador.textContent = produtos.length ? `${produtos.length} produto${produtos.length !== 1 ? 's' : ''}` : '';

    if (!produtos.length) {
        container.innerHTML = '<p class="mensagem-vazia">Nenhum produto encontrado nesta categoria.</p>';
    } else {
        container.innerHTML = produtos.map(criarCardProduto).join('');
    }

    // Ao trocar de categoria, rola até o topo da área de produtos
    const alvo = document.querySelector('.produtos-area');
    if (alvo) {
        // Compensa a altura do header fixo (sticky)
        const header = document.querySelector('.header');
        const offset = header ? header.offsetHeight + 12 : 12;
        const topo = alvo.getBoundingClientRect().top + window.pageYOffset - offset;
        window.scrollTo({ top: topo, behavior: 'smooth' });
    }
}

// Inicia ao carregar a página
document.addEventListener('DOMContentLoaded', () => {
    carregarCategorias();
    // Carrega os produtos da primeira seleção (Todos)
    const ativo = document.querySelector('.categoria-btn.active');
    if (ativo) selecionarCategoria(ativo);
});