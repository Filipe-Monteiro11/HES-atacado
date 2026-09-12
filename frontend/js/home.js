// =============================================
// HES ATACADO — Home (destaques + funções gerais)
// =============================================

document.addEventListener('DOMContentLoaded', function () {
    // Ano do rodapé
    const ano = document.getElementById('ano');
    if (ano) ano.textContent = new Date().getFullYear();

    // Elementos do carrossel
    const grid = document.getElementById('produtosDestaque');
    const prevBtn = document.getElementById('destaquePrev');
    const nextBtn = document.getElementById('destaqueNext');

    let destaques = [];
    let indice = 0;

    async function carregarDestaques() {
        try {
            const res = await fetch('/api/produtos/');
            const data = await res.json();
            const produtos = Array.isArray(data) ? data : (data.results || []);
            destaques = produtos.filter(p => p.destaque);
            if (destaques.length === 0) {
                grid.innerHTML = '<p class="sem-produtos">Nenhum produto em destaque no momento.</p>';
                return;
            }
            renderizar();
        } catch (err) {
            grid.innerHTML = '<p class="sem-produtos">Não foi possível carregar os produtos.</p>';
        }
    }

    function renderizar() {
        const p = destaques[indice];
        const imagem = p.imagem
            ? `<img src="${p.imagem}" alt="${p.nome}" loading="lazy">`
            : `<div class="sem-imagem"><i class="fa-solid fa-box"></i></div>`;
        grid.innerHTML = `
            <div class="produto-card">
                <div class="produto-img">${imagem}</div>
                <div class="produto-info">
                    <h3 class="produto-nome">${p.nome}</h3>
                    ${p.descricao ? `<p class="produto-desc">${p.descricao}</p>` : ''}
                </div>
            </div>`;
    }

    // Seta esquerda → produto anterior (volta ao fim quando chega no início)
    prevBtn.addEventListener('click', () => {
        if (!destaques.length) return;
        indice = (indice - 1 + destaques.length) % destaques.length;
        renderizar();
    });

    // Seta direita → próximo produto (volta ao início quando chega no fim)
    nextBtn.addEventListener('click', () => {
        if (!destaques.length) return;
        indice = (indice + 1) % destaques.length;
        renderizar();
    });

    carregarDestaques();
});