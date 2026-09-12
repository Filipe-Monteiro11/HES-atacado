// =============================================
// HES ATACADO — Home (destaques + funções gerais)
// =============================================

document.addEventListener('DOMContentLoaded', function () {
    // Ano do rodapé
    const ano = document.getElementById('ano');
    if (ano) ano.textContent = new Date().getFullYear();

    // Elementos do carrossel
    const track = document.getElementById('produtosDestaque');
    const prevBtn = document.getElementById('destaquePrev');
    const nextBtn = document.getElementById('destaqueNext');
    const counter = document.getElementById('destaqueCounter');
    if (!track) return;

    let slides = [];
    let indice = 0;
    let startX = null;

    const esc = (s) => String(s == null ? '' : s)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;');

    // Encurta a categoria: "Tratamento de Piso — Pluron" -> "Tratamento de Piso"
    function nomeCategoria(p) {
        const bruto = p.categoria || p.subcategoria || p.categoria_nome || p.subcategoria_nome || '';
        return String(bruto).split(/\s+[—–-]\s+/)[0].trim();
    }

    function renderSlide(p) {
        const nome = esc(p.nome);
        const cat = esc(nomeCategoria(p));
        const imagem = p.imagem
            ? `<img src="${p.imagem}" alt="${nome}" loading="lazy">`
            : `<div class="placeholder"><i class="fa-regular fa-image"></i><span>Imagem em breve</span></div>`;
        const desc = p.descricao ? `<p class="destaque-desc">${esc(p.descricao)}</p>` : '';

        return `
            <div class="destaque-slide">
                <article class="destaque-card">
                    <div class="destaque-img">${imagem}</div>
                    <div class="destaque-info">
                        ${cat ? `<span class="destaque-tag">${cat}</span>` : ''}
                        <h3 class="destaque-nome">${nome}</h3>
                        ${desc}
                        <a class="destaque-cta" href="/produtos/">Ver produtos <i class="fa-solid fa-arrow-right"></i></a>
                    </div>
                </article>
            </div>`;
    }

    function atualizar() {
        track.style.transform = `translateX(-${indice * 100}%)`;
        if (counter) counter.textContent = `${indice + 1} / ${slides.length}`;
    }

    function ir(delta) {
        if (slides.length < 2) return;
        indice = (indice + delta + slides.length) % slides.length;
        atualizar();
    }

    async function carregar() {
        try {
            const res = await fetch('/api/produtos/');
            const data = await res.json();
            const produtos = Array.isArray(data) ? data : (data.results || []);
            slides = produtos.filter(p => p.destaque);

            if (!slides.length) {
                track.innerHTML = '<p class="sem-produtos">Nenhum produto em destaque no momento.</p>';
                if (counter) counter.textContent = '';
                return;
            }
            track.innerHTML = slides.map(renderSlide).join('');
            atualizar();
        } catch (err) {
            track.innerHTML = '<p class="sem-produtos">Não foi possível carregar os destaques.</p>';
        }
    }

    prevBtn.addEventListener('click', () => ir(-1));
    nextBtn.addEventListener('click', () => ir(1));

    // Navegação pelo teclado
    document.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowLeft') ir(-1);
        if (e.key === 'ArrowRight') ir(1);
    });

    // Arrastar no celular
    track.addEventListener('touchstart', (e) => {
        startX = e.touches[0].clientX;
    }, { passive: true });

    track.addEventListener('touchend', (e) => {
        if (startX === null) return;
        const dx = e.changedTouches[0].clientX - startX;
        if (Math.abs(dx) > 40) ir(dx < 0 ? 1 : -1);
        startX = null;
    }, { passive: true });

    carregar();
});