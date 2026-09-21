// =============================================
// HES ATACADO — Página de Produtos
// Categoria na sidebar → mostra os produtos dela
// =============================================

// Ano automático no rodapé
const ano = document.getElementById('ano');
if (ano) ano.textContent = new Date().getFullYear();

// ---------------------------------------------
// FOTO DE BANNER AUTOMÁTICA POR CATEGORIA
// O nome do arquivo é o nome da categoria "limpo":
//   minúsculas, sem acento. Aceita COM ESPAÇO ou COM HÍFEN:
//   Ex.: "Laticínios"                  -> laticinios.png
//        "Higiene Pessoal / Institucional" -> higiene pessoal institucional.png
//                                          (ou higiene-pessoal-institucional.png)
// Basta colocar a imagem em static/img/ com esse nome.
// Se o arquivo tiver outro nome (ou erro de digitação), use o ALIASES abaixo.
// Se não existir imagem pra categoria, fica o visual padrão.
// ---------------------------------------------
const PASTA_BANNERS = '/static/img/';
const EXTENSOES = ['webp', 'png', 'jpg', 'jpeg'];   // formatos aceitos (ordem = prioridade)
const cacheFundos = {};
let categoriaAtual = '';

// Categorias cujo arquivo NÃO tem o nome da categoria.
// Chave = slug da categoria | Valor = lista de nomes de arquivo (sem extensão, IGUAL ao arquivo)
const ALIASES = {
    // As 3 linhas de dispensers usam a mesma imagem: dispensers.png
    'dispensers-linha-gold':     ['dispensers'],
    'dispensers-linha-care':     ['dispensers'],
    'dispensers-linha-standart': ['dispensers'],

    'equipamentos-sistemas-de-limpeza-profissional': ['equipamentos sistemas de limpesa profissional'],
    'equipamentos-de-limpeza-profissional':          ['equipamentos sistemas de limpesa profissional'],
    'farmaceutica-e-hospitalar':                     ['farmaceutica e hospitala'],
    'cozinha-industrial-e-restaurantes-lava-loucas': ['cozinha industrial'],
    'detergente-sanitizante-em-po':                  ['detergente sitantizante em Pó']
};

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

    // nomes a testar, em ordem de prioridade:
    // 1) apelido  2) nome com espaços  3) nome com hífen
    const nomes = [
        ...(ALIASES[slug] || []),
        slug.replace(/-/g, ' '),
        slug
    ];

    // monta todas as combinações nome × extensão e testa tudo ao mesmo tempo
    const urls = [];
    for (const nome of new Set(nomes)) {
        for (const ext of EXTENSOES) {
            urls.push(encodeURI(`${PASTA_BANNERS}${nome}.${ext}`));
        }
    }

    const resultados = await Promise.all(urls.map(testarImagem));
    const achou = resultados.indexOf(true);   // primeira na ordem de prioridade

    cacheFundos[slug] = achou !== -1 ? urls[achou] : null;
    return cacheFundos[slug];
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

// ---------------------------------------------
// LEMBRAR A CATEGORIA ESCOLHIDA
// A categoria fica guardada na URL (?categoria=ID).
// Assim, ao abrir um produto e voltar, a página abre
// na mesma categoria (e na mesma posição de rolagem).
// ---------------------------------------------
const botaoTodos = document.querySelector('.categoria-btn.active');   // "Todos os produtos"

function salvarCategoriaNaURL(botao) {
    const url = new URL(window.location.href);
    if (botao === botaoTodos) {
        url.searchParams.delete('categoria');
    } else {
        url.searchParams.set('categoria', botao.dataset.categoria);
    }
    history.replaceState(null, '', url);
}

function categoriaSalva() {
    return new URLSearchParams(window.location.search).get('categoria');
}

// guarda a posição da rolagem quando clica num produto
document.addEventListener('click', (e) => {
    if (e.target.closest('.produto-card')) {
        sessionStorage.setItem('hes_scroll', JSON.stringify({
            categoria: categoriaSalva() || '',
            y: window.pageYOffset
        }));
    }
});

function lerScrollSalvo() {
    try {
        const salvo = JSON.parse(sessionStorage.getItem('hes_scroll'));
        sessionStorage.removeItem('hes_scroll');
        if (salvo && salvo.categoria === (categoriaSalva() || '')) return salvo.y;
    } catch (e) { /* ignora */ }
    return null;
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
if (botaoTodos) {
    botaoTodos.addEventListener('click', () => selecionarCategoria(botaoTodos));
}

// Seleciona uma categoria e carrega os produtos dela
// opcoes.inicial = true → é a abertura da página (não rola pro topo)
async function selecionarCategoria(botao, opcoes = {}) {
    document.querySelectorAll('.categoria-btn').forEach(b => b.classList.remove('active'));
    botao.classList.add('active');

    const categoriaId = botao.dataset.categoria;
    const nome = botao.dataset.nome || 'Todos os Produtos';
    document.getElementById('tituloCategoria').textContent = nome;

    salvarCategoriaNaURL(botao);

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

    // Abertura da página: volta pra posição onde o usuário estava (se houver)
    if (opcoes.inicial) {
        const y = lerScrollSalvo();
        if (y !== null) window.scrollTo({ top: y, behavior: 'instant' });
        return;
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
document.addEventListener('DOMContentLoaded', async () => {
    // espera as categorias carregarem para poder reabrir a que estava salva
    await carregarCategorias();

    let botao = botaoTodos;
    const salva = categoriaSalva();
    if (salva) {
        const encontrado = [...document.querySelectorAll('.categoria-btn')]
            .find(b => b.dataset.categoria === salva);
        if (encontrado) botao = encontrado;
    }

    if (botao) selecionarCategoria(botao, { inicial: true });
});