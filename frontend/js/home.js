document.addEventListener('DOMContentLoaded', function () {
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

    function nomeDe(p) {
        return p.nome || p.name || p.titulo || '';
    }
    function imagemDe(p) {
        return p.imagem || p.imagem_url || p.foto || p.image || null;
    }
    function categoriaDe(p) {
        const bruto = p.categoria || p.subcategoria || p.categoria_nome || '';
        return String(bruto).split(/\s+[—–-]\s+/)[0].trim();
    }
    function ehDestaque(p) {
        const v = p.destaque ?? p.em_destaque ?? p.is_destaque;
        return v === true || v === 1 || v === '1' || v === 'true' || v === 'sim';
    }

    function renderCard(p) {
        const nome = esc(nomeDe(p));
        const cat = esc(categoriaDe(p));
        const img = imagemDe(p);
        const idCat = p.categoria_id || '';
        const link = `/produtos/?categoria=${idCat}`;
        const imagem = img
            ? `<img src="${img}" alt="${nome}" loading="lazy" draggable="false">`
            : `<div class="placeholder"><i class="fa-regular fa-image"></i><span>Imagem em breve</span></div>`;
        return `
            <a href="${link}" class="feed-card" data-categoria="${idCat}">
                <div class="feed-img">${imagem}</div>
                <div class="feed-body">
                    ${cat ? `<span class="feed-tag">${cat}</span>` : ''}
                    <h3 class="feed-nome">${nome}</h3>
                </div>
            </a>`;
    }

    function atualizar() {
        const N = produtos.length;
        const metade = Math.floor(N / 2);
        const cards = stage.querySelectorAll('.feed-card');
        cards.forEach((card, i) => {
            card.className = 'feed-card';
            // distância circular até o card ativo (funciona com qualquer quantidade)
            const diff = ((i - ativo + N + metade) % N) - metade;

            if (diff === 0) card.classList.add('active');
            else if (diff === -1) card.classList.add('left-1');
            else if (diff === -2) card.classList.add('left-2');
            else if (diff === 1) card.classList.add('right-1');
            else if (diff === 2) card.classList.add('right-2');
            else card.classList.add('hidden');
        });
        if (counter) counter.textContent = `${ativo + 1} / ${N}`;
    }

    function ir(delta) {
        if (produtos.length < 2) return;
        ativo = (ativo + delta + produtos.length) % produtos.length;
        atualizar();
    }

    async function carregar() {
        try {
            const res = await fetch('/api/produtos/?destaque=1');
            const data = await res.json();
            const lista = Array.isArray(data) ? data : (data.results || []);
            produtos = lista.filter(ehDestaque);

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

    // Clique num card lateral: traz ele para o centro (só o central abre o link)
    stage.addEventListener('click', (e) => {
        const card = e.target.closest('.feed-card');
        if (!card || card.classList.contains('active')) return;
        e.preventDefault();
        const cards = Array.from(stage.querySelectorAll('.feed-card'));
        ativo = cards.indexOf(card);
        atualizar();
    });

    // Swipe no celular
    let x0 = null;
    stage.addEventListener('touchstart', (e) => { x0 = e.touches[0].clientX; }, { passive: true });
    stage.addEventListener('touchend', (e) => {
        if (x0 === null) return;
        const dx = e.changedTouches[0].clientX - x0;
        if (Math.abs(dx) > 40) ir(dx < 0 ? 1 : -1);
        x0 = null;
    });

    if (prevBtn) prevBtn.addEventListener('click', () => ir(-1));
    if (nextBtn) nextBtn.addEventListener('click', () => ir(1));

    document.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowLeft') ir(-1);
        if (e.key === 'ArrowRight') ir(1);
    });

    carregar();
});