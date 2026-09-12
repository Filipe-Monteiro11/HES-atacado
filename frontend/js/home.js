document.addEventListener('DOMContentLoaded', function () {
    // Ano do rodapé
    const ano = document.getElementById('ano');
    if (ano) ano.textContent = new Date().getFullYear();

    const stage = document.getElementById('feedStage');
    const prevBtn = document.getElementById('feedPrev');
    const nextBtn = document.getElementById('feedNext');
    const counter = document.getElementById('feedCounter');
    if (!stage) return;

    let produtos = [];
    let ativo = 0;

    const esc = (s) => String(s == null ? '' : s)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;');

    function nomeCategoria(p) {
        const bruto = p.categoria || p.subcategoria || p.categoria_nome || p.subcategoria_nome || '';
        return String(bruto).split(/\s+[—–-]\s+/)[0].trim();
    }

    function renderCard(p) {
        const nome = esc(p.nome);
        const cat = esc(nomeCategoria(p));
        const imagem = p.imagem
            ? `<img src="${p.imagem}" alt="${nome}" loading="lazy">`
            : `<div class="placeholder"><i class="fa-regular fa-image"></i><span>Imagem em breve</span></div>`;
        return `
            <article class="feed-card">
                <div class="feed-img">${imagem}</div>
                <div class="feed-body">
                    ${cat ? `<span class="feed-tag">${cat}</span>` : ''}
                    <h3 class="feed-nome">${nome}</h3>
                </div>
            </article>`;
    }

    // Atribui a posição visual de cada card com base no índice ativo
    function atualizar() {
        const cards = stage.querySelectorAll('.feed-card');
        cards.forEach((card, i) => {
            card.className = 'feed-card';
            let diff = i - ativo;
            // normaliza para o intervalo -2..2
            if (diff < -2) diff += produtos.length;
            if (diff > 2) diff -= produtos.length;

            if (diff === 0) card.classList.add('active');
            else if (diff === -1) card.classList.add('left-1');
            else if (diff === -2) card.classList.add('left-2');
            else if (diff === 1) card.classList.add('right-1');
            else if (diff === 2) card.classList.add('right-2');
            else card.classList.add('hidden');
        });
        if (counter) counter.textContent = `${ativo + 1} / ${produtos.length}`;
    }

    function ir(delta) {
        if (produtos.length < 2) return;
        ativo = (ativo + delta + produtos.length) % produtos.length;
        atualizar();
    }

    async function carregar() {
        try {
            const res = await fetch('/api/produtos/');
            const data = await res.json();
            const lista = Array.isArray(data) ? data : (data.results || []);
            produtos = lista.filter(p => p.destaque);

            if (!produtos.length) {
                stage.innerHTML = '<p class="sem-produtos">Nenhum produto em destaque no momento.</p>';
                if (counter) counter.textContent = '';
                return;
            }
            stage.innerHTML = produtos.map(renderCard).join('');
            atualizar();
        } catch (err) {
            stage.innerHTML = '<p class="sem-produtos">Não foi possível carregar os destaques.</p>';
        }
    }

    prevBtn.addEventListener('click', () => ir(-1));
    nextBtn.addEventListener('click', () => ir(1));

    // Navegação pelo teclado
    document.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowLeft') ir(-1);
        if (e.key === 'ArrowRight') ir(1);
    });

    carregar();
});