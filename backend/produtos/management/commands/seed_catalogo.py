# -*- coding: utf-8 -*-
"""
Seed do catálogo HES Hygiene Solutions.

Cria cada tópico do catálogo como Categoria e todos os produtos de cada tópico,
com a descrição/área de uso de cada um. Produtos podem aparecer em mais de um
tópico (ex: PLURON 7160 em Desincrustantes e em Lavanderia) - por isso a busca
usa (nome + subcategoria), e nao apenas o nome.

Uso:
    python manage.py seed_catalogo            # cria/atualiza sem duplicar
    python manage.py seed_catalogo --reset    # APAGA categorias/produtos e recria
"""
from django.core.management.base import BaseCommand
from django.db import transaction
from produtos.models import Categoria, Subcategoria, Produto

CATALOGO = [
    # ============================================================
    # 1. DISPENSERS — LINHA GOLD
    # ============================================================
    ("Dispensers — Linha Gold",
     "Linha premium de dispensers com design sofisticado, alta durabilidade e acabamento elegante para ambientes profissionais e corporativos.",
     [
        ("Dispenser Sabonete Espuma", "Acionamento por bomba e dosagem controlada; acabamento premium para banheiros de alto padrão."),
        ("Dispenser Sabonete Líquido", "Alta capacidade, com válvula dosadora e design sofisticado."),
        ("Dispenser Papel Toalha Bobina", "Sistema de corte e proteção contra umidade; indicado para alto fluxo."),
        ("Dispenser Papel Toalha Interfolhado", "Retirada folha a folha, reduz desperdício e protege o papel."),
        ("Dispenser Papel Toalha Interfolhado Mini", "Versão compacta, para espaços reduzidos mantendo a praticidade."),
        ("Dispenser Coletor de Absorvente", "Tampa que isola resíduos e odores na cabine."),
        ("Dispenser Guardanapeira Interfolhada", "Libera um guardanapo por vez."),
        ("Dispenser Papel Higiênico", "Modelos em rolo e interfolhado, com proteção contra contaminação e reposição prática."),
     ]),

    # ============================================================
    # 2. DISPENSERS — LINHA CARE
    # ============================================================
    ("Dispensers — Linha Care",
     "Linha com design suave e funcional, oferecendo segurança, higiene e praticidade para hospitais, clínicas e ambientes institucionais.",
     [
        ("Dispenser Sabonete Espuma Care", "Design suave e funcional para hospitais e clínicas."),
        ("Dispenser Sabonete Líquido Care", "Acionamento ergonômico, voltado à higiene institucional."),
        ("Dispenser Papel Toalha Bobina Care", "Corte facilitado e estrutura resistente."),
        ("Dispenser Papel Toalha Interfolhado Care", "Retirada individual e higiênica."),
        ("Dispenser Papel Toalha Interfolhado Mini Care", "Indicado para banheiros de menor circulação."),
        ("Dispenser Papel Higiênico Rolo Care", "Tampa de proteção e encaixe seguro."),
        ("Dispenser Coletor de Absorvente Care", "Descarte isolado, contribuindo para a higiene e o bom odor do ambiente."),
        ("Dispenser Guardanapeira Interfolhada Care", "Liberação de uma folha por vez."),
        ("Dispenser Papel Higiênico Linha Care", "Sistema de recarga prática e encaixe seguro."),
     ]),

    # ============================================================
    # 3. DISPENSERS — LINHA STANDART
    # ============================================================
    ("Dispensers — Linha Standart",
     "Funcionalidade, durabilidade e praticidade em design versátil, proporcionando mais higiene, segurança e economia.",
     [
        ("Dispenser Sabonete Líquido Standart", "Funcionalidade, durabilidade e bom custo-benefício."),
        ("Dispenser Sabonete Espuma Standart", "Acionamento simples e manutenção fácil."),
        ("Dispenser Papel Toalha Bobina Standart", "Estrutura versátil e resistente."),
        ("Dispenser Papel Toalha Interfolhado Standart", "Prático e econômico."),
        ("Dispenser Papel Toalha Interfolhado Mini Standart", "Compacto, ideal para ambientes com espaço reduzido."),
        ("Dispenser Papel Higiênico Rolo Standart", "Instalação e reposição simples."),
        ("Dispenser Coletor de Absorvente Standart", "Descarte higiênico em cabines sanitárias."),
        ("Dispenser Guardanapeira Interfolhada Standart", "Operação simples, uso institucional."),
        ("Dispenser Papel Higiênico Linha Standart", "Reposição prática para uso contínuo."),
     ]),

    # ============================================================
    # 4. EQUIPAMENTOS PROFISSIONAIS
    # ============================================================
    ("Equipamentos Profissionais",
     "Equipamentos para alto desempenho, segurança e eficiência em ambientes industriais, comerciais e de serviços.",
     [
        ("Diluidores", "Instalação de diluidores de produtos químicos concentrados com sistema Venturi, permitindo diluições precisas via TIP."),
        ("Dosadores", "Dosadores individuais utilizados na higienização de máquinas de lavar louça e lavanderias."),
        ("Treinamento", "Treinamentos completos para uso correto e seguro dos produtos e equipamentos fornecidos."),
     ]),

    # ============================================================
    # 5. LINHA DE PAPÉIS INSTITUCIONAIS
    # ============================================================
    ("Linha de Papéis Institucionais",
     "Alta absorção, resistência e suavidade, com responsabilidade ecológica.",
     [
        ("Papel Toalha Bobina 200M", "Papel toalha em bobina de 200 m, com alta absorção e resistência; caixa com 6 unidades."),
        ("Papel Toalha Bobina 150M", "Papel toalha em bobina de 150 m, macio e resistente; caixa com 6 unidades."),
        ("Toalha Interfolhada 2 Dobras", "20 x 21 cm, 2 dobras, absorvente e suave; 8.000 folhas por caixa."),
        ("Toalha Interfolhada 3 Dobras", "22 x 23 cm, 3 dobras, maior resistência; 2.400 folhas por caixa."),
        ("Higiênico Bobina Folha Dupla", "10 cm x 300 m; macio e resistente."),
        ("Higiênico Bobina Folha Simples", "10 cm x 300 m; econômico e resistente."),
        ("Higiênico Interfolhado Folha Dupla", "20 x 21 cm, 1.000 folhas; suave e absorvente."),
        ("Higiênico Interfolhado", "10 x 21 cm, 8.000 folhas; macio e econômico para alto volume."),
     ]),

    # ============================================================
    # 6. HIGIENE PESSOAL — SABONETES E ANTISSÉPTICOS
    # ============================================================
    ("Higiene Pessoal e Sabonetes",
     "Linha completa de limpeza de alta qualidade para escolas, hotéis, motéis, supermercados e espaços institucionais.",
     [
        ("Pluron Clorexidine", "Sabonete perfumado para aplicação por espuma e/ou spray, indicado para limpeza das mãos."),
        ("Pluron Handmax Erva Doce", "Sabonete com glicerina e alcanolamida que evita o ressecamento da pele mesmo com uso frequente."),
        ("Pluron 7060 M", "Sabonete para limpeza de graxas e óleos das mãos em oficinas mecânicas e indústrias."),
        ("Pluron 7230", "Limpa pisos, paredes, equipamentos e caixas plásticas em indústrias; fórmula concentrada de rápida penetração."),
        ("Pluron Handmax Blue", "Limpeza de mãos com perfume floral; fórmula concentrada e econômica."),
        ("Pluron 144 A Sept", "Contém triclosan, promovendo proteção e inibindo microrganismos na pele."),
        ("Pluron Foam Hand Sept", "Limpeza e assepsia das mãos, com formulação específica para dispensers de espuma."),
        ("Pluron Top Remove", "Remove ceras e sujidades em Paviflex, Plurigoma, Ardósia, Pedras Naturais, Granilite e Mármore (exceto madeira)."),
        ("Pluron Handfoam", "Sabonete perfumado por espuma; versões Cereja e Avelã, Pêssego e Erva Doce."),
        ("Pluron 147 AG", "Álcool gel 70% antisséptico das mãos, sem necessidade de enxágue."),
        ("Pluron Álcool Foam", "Antisséptico das mãos por espuma, sem necessidade de enxágue."),
        ("Pluron 147 BG Sept", "Álcool 70% com clorexidina para assepsia das mãos."),
     ]),

    # ============================================================
    # 7. TRATAMENTO DE PISO
    # ============================================================
    ("Tratamento de Piso",
     "Produtos para selamento, brilho e limpeza de pisos laváveis: mármore, cerâmica, porcelanato, Paviflex, granilite e outros.",
     [
        ("Pluron Selafix", "Base seladora para área interna; antiderrapante e não inflamável."),
        ("Pluron Selafix EX", "Base seladora para área interna e externa; resistente ao tráfego."),
        ("Pluron Maxbrilho AT", "Cera auto brilho e impermeabilizante para pisos laváveis; dispensa enceradeira."),
        ("Pluron 7914", "Cera auto brilhante, antiderrapante e resistente ao tráfego."),
        ("Pluron Top Brilho", "Cera 3x1: sela, dá brilho e protege; alta aderência e efeito antiderrapante."),
        ("Pluron 7215", "Limpeza de pisos de mármore, borracha, cerâmica e plásticos com lavadoras automáticas."),
        ("Pluron 7225", "Remove ceras de pisos porosos (exceto madeira) e sujidades de terras em pisos frios encardidos."),
        ("Pluron H8 Premium", "Elimina cheiro de tabaco e atua como odorizante de ambiente."),
        ("Pluron H3 Herbal", "Limpeza de pisos de mármore, borracha, cerâmica e plástico com mop ou lavadoras automáticas."),
        ("Pluron H2 Premium", "Limpador de vasos sanitários; remove manchas de sais de cálcio, magnésio e ferro."),
        ("Pluron H4 Marine", "Limpeza manual de pisos e superfícies impregnadas com gorduras ou sujidades arenosas."),
        ("Pluron H5 Premium", "Detergente perfumado para limpeza pesada de piso e superfícies engorduradas."),
        ("Pluron H4 Premium", "Limpeza manual de pisos e superfícies com gorduras ou sujidades arenosas."),
        ("Pluron Multi Citronela", "Contém citronela, afastando insetos como moscas e mosquitos."),
        ("Pluron Multi Porcelanato", "Baixa espumação, indicado para pisos de porcelanato e outros tipos."),
     ]),

    # ============================================================
    # 8. LIMPADORES PERFUMADOS E ODORIZANTES
    # ============================================================
    ("Limpadores Perfumados e Odorizantes",
     "Limpadores de uso geral, perfumados e odorizantes para pisos, vidros, superfícies e ambientes.",
     [
        ("Pluron Limpador Capim Limão", "Limpeza manual de pisos laváveis e superfícies de residências, hospitais, condomínios, shoppings, escolas e hotéis."),
        ("Pluron Limpador Pitanga", "Deixa agradável perfume no ambiente."),
        ("Pluron Trioxy", "Concentrado à base de peróxido de hidrogênio e tensoativos; limpeza geral e alvejamento, com ação contra mofo."),
        ("Pluron 7470", "Limpeza diária de vidros, espelhos, acrílicos, azulejos, fórmica e superfícies de plástico, metal e courvin."),
        ("Pluron Sanit", "Linhas Eucalipto, Floral, Floral Fresh, Intense Floral, Intense Summer, Intense Marine, Lavanda, Marine, Top Floral e Top Lavanda; com ativos bactericidas contra Staphylococcus aureus e Salmonella choleraesuis, além de perfumar o ambiente."),
     ]),

    # ============================================================
    # 9. DESINFETANTES PERFUMADOS
    # ============================================================
    ("Desinfetantes Perfumados",
     "Desinfetantes com ação bactericida e perfume agradável para pisos e superfícies em geral.",
     [
        ("Pluron Sanit Top Floral / Top Lavanda", "Ação bactericida que desinfeta, limpa e odoriza; à base de quaternário de amônio, eficaz inclusive contra Coronavírus cepa MHV."),
     ]),

    # ============================================================
    # 10. DETERGENTES PERFUMADOS
    # ============================================================
    ("Detergentes Perfumados",
     "Detergentes perfumados para limpeza de equipamentos, superfícies, pisos e ambientes.",
     [
        ("Pollyclean 10.000", "Detergente flotador para limpeza de equipamentos de cozinhas, pias, fogão, fôrmicas, plástico, banheiro, pisos, azulejos, balcões, cerâmica e mesas de mármore."),
        ("Pluron Sanit Lavanda / Marine", "Detergentes/desinfetantes perfumados com ativos bactericidas."),
     ]),

    # ============================================================
    # 11. DESINCRUSTANTES E LIMPA ALUMÍNIO
    # ============================================================
    ("Desincrustantes e Limpa Alumínio",
     "Produtos para desincrustação de gorduras carbonizadas e limpeza de utensílios de alumínio.",
     [
        ("Pluron 7160", "Lava e desengordura pisos, fogões, exaustores, pias, azulejos, geladeiras e banheiros."),
        ("Pluron 7710 AE", "Limpeza por espuma de equipamentos e superfícies impregnadas com gorduras carbonizadas e resíduos oleosos."),
        ("Pluron 236 A", "Limpeza e desincrustação de formas, latões, caixas plásticas, garrafas, louças e ordenhadeiras mecânicas."),
        ("Pluron 7756", "Higienização de pratos, talheres, bandejas, copos e xícaras em máquinas de lavar."),
        ("Pluron 7799 A", "Enxágue final de máquinas de lavar louças; promove secagem rápida e evita manchas."),
        ("Pluron 7888", "Desinfetante para frutas, legumes e verduras; ampla ação biocida contra Enterococcus faecium e Escherichia coli."),
        ("Pluron Versat", "Limpeza de gorduras carbonizadas em utensílios de alumínio (panelas, coifas, frigideiras, assadeiras)."),
        ("Pluron LA 21", "Detergente ácido para limpeza e brilho de utensílios de alumínio."),
     ]),

    # ============================================================
    # 12. COZINHA INDUSTRIAL E RESTAURANTES
    # ============================================================
    ("Cozinha Industrial e Restaurantes",
     "Linha formulada para as demandas rigorosas de cozinhas industriais, bares, restaurantes, padarias e açougues.",
     [
        ("Pluron Top Grill", "Limpeza de fornos, grelhas, chapas, frigideiras e superfícies com gordura carbonizada."),
        ("Pluron 7799 A Cozinha", "Enxágue final para secagem rápida e eliminação de manchas."),
        ("Pluron Maq Duo", "2x1 para lavagem e secagem de louças em máquinas."),
        ("Pluron Maq Det", "Limpeza de pratos, talheres, bandejas, copos e xícaras em máquinas de lavar."),
        ("Pluron Maq Sec", "Enxágue final para secagem rápida e eliminação de manchas."),
        ("Pluron Maq Clor", "Limpeza de louças e utensílios em máquinas de lavar."),
        ("Pluron 194 A", "Detergente neutro para utensílios, pisos, paredes, latões, tanques e mesas de trabalho."),
        ("Pluron 194 AV", "Detergente neutro para utensílios, pisos, paredes, latões, tanques e mesas de trabalho."),
        ("Pluron 404 A", "Limpeza manual de pisos, paredes, latões, tanques, louças e utensílios em indústrias alimentícias."),
        ("Pluron 406 A", "Limpeza manual de pisos, paredes, latões, tanques, louças e utensílios em indústrias alimentícias."),
        ("Pluron Detergente Neutro", "Reduz a tensão superficial, facilitando a remoção de gordura."),
        ("Pluron 7888 Em Pó", "Detergente/sanitizante em pó."),
     ]),

    # ============================================================
    # 13. LATICÍNIOS
    # ============================================================
    ("Laticínios",
     "Produtos específicos para limpeza e desinfecção de toda a cadeia do leite: ordenha, tanques, armazenamento e pasteurizadores.",
     [
        ("Pluron Alcali Clor", "Baixa espuma para limpeza CIP de ordenhadeiras, tanques, misturadores, resfriadores e tubulações; também para post-mix e chopeiras."),
        ("Pluron Clorcip", "Baixa espuma para limpeza CIP de ordenhadeiras, pisos, paredes, equipamentos e garrafões em indústrias de águas minerais."),
        ("Pluron 236 A Laticínios", "Limpeza e desincrustação de formas, latões, caixas plásticas, garrafas e ordenhadeiras."),
        ("Pluron 426 A", "Uso manual e por circulação para pisos, paredes, latões, tanques de recepção, resfriadores e equipamentos."),
        ("Pluron 327 AS", "Limpeza por circulação (CIP) de tanques, equipamentos e tubulações."),
        ("Pluron 327 CIP", "Limpeza por circulação (CIP) de tanques, equipamentos e tubulações."),
        ("Pluron 337 AB", "Limpeza de ganchos, carretilhas, garrafas e circulação de pasteurizadores, evaporadores e resfriadores."),
        ("Pluron Detaclor Laticínios", "Limpeza manual ou por espuma de equipamentos com gorduras e resíduos oleosos."),
        ("Pluron Clorofoam AL", "Limpeza por espuma de superfícies com gorduras e resíduos oleosos."),
        ("Pluron 489 AT5", "Limpeza manual ou por espuma de equipamentos e superfícies engorduradas."),
        ("Pluron 428 A4", "Limpeza manual ou por espuma de equipamentos e superfícies engorduradas."),
        ("Pluron Nitric", "Ácido de baixa espuma para circulação de pasteurizadores, concentradores, evaporadores e desincrustação de gordura carbonizada."),
        ("Pluron 320 A", "Limpeza ácida de tanques de fermentação e maturação de cerveja, tubulações e pasteurizadores."),
        ("Pluron TS 787 B", "Limpeza por circulação nas linhas de troca de sabores e circuitos post-mix."),
        ("Pluron 418 A", "Limpeza por espuma de superfícies com gorduras e resíduos de óleos."),
        ("Pluron 446 A", "Limpeza de pisos, azulejos de cozinhas e equipamentos em geral."),
        ("Pluron 950 Pack", "Limpa e lubrifica esteiras e correntes de transporte de embalagens cartonadas."),
        ("Pluron 447 AE", "Detergente/desincrustante ácido para gorduras, proteínas e sujidades inorgânicas."),
        ("Pluron 489 A", "Detergente/desincrustante ácido para gorduras, proteínas e sujidades inorgânicas."),
        ("Pluron 490 A", "Detergente/desincrustante ácido para gorduras, proteínas e sujidades inorgânicas."),
        ("Pluron 490 AM", "Detergente/desincrustante ácido para gorduras, proteínas e sujidades inorgânicas."),
        ("Pluron Acid Foam", "Detergente ácido para limpeza externa; remove Pedra Cervejeira (Oxalato de Cálcio) e Pedra de Leite (Fosfato Tricálcico)."),
        ("Pluron 786 B5", "Aditivo para soluções cáusticas e ácidas em CIP e lavagem de garrafas; antiespumante."),
        ("Pluron CE 800 B", "Aditivo para soluções cáusticas e ácidas em CIP e lavagem de garrafas; antiespumante."),
        ("Pluron 461 A1", "Desinfetante para equipamentos, tanques, válvulas, tubulações, pisos e paredes em indústrias de alimentos."),
        ("Pluron 463 AP", "Desinfetante para equipamentos, tanques, válvulas, tubulações, pisos e paredes em indústrias de alimentos."),
        ("Pluron Hidroxysept", "Desinfetante para equipamentos, tanques, válvulas, tubulações, pisos e paredes em indústrias de alimentos."),
     ]),

    # ============================================================
    # 14. FRIGORÍFICOS E ABATEDOUROS
    # ============================================================
    ("Frigoríficos e Abatedouros",
     "Linha desenvolvida para atender às normas de higiene dos Ministérios da Saúde e da Agricultura em frigoríficos e abatedouros.",
     [
        ("Pluron 199 A1", "Imersão para proteção de ganchos e carretilhas de ferro/aço contra oxidação; fosfatização de superfícies metálicas."),
        ("Pluron 199 A2", "Imersão para proteção de ganchos e carretilhas de ferro/aço contra oxidação; fosfatização de superfícies metálicas."),
        ("Pluron 488 A", "Limpeza por imersão de cozinhadores contínuos/estáticos, ganchos e carretilhas."),
        ("Pluron 484 A", "Limpeza manual de pisos, paredes, latões, tanques, equipamentos, botas, luvas e utensílios em indústrias alimentícias e farmacêuticas."),
        ("Pluron 485 A", "Limpeza manual de pisos, paredes, latões, tanques, equipamentos, botas, luvas e utensílios em indústrias alimentícias e farmacêuticas."),
        ("Pluron 485 A SE", "Limpeza manual de pisos, paredes, latões, tanques, equipamentos, botas, luvas e utensílios em indústrias alimentícias e farmacêuticas."),
        ("Pluron 485 AE", "Limpeza manual de pisos, paredes, latões, tanques, equipamentos, botas, luvas e utensílios em indústrias alimentícias e farmacêuticas."),
        ("Pluron Álcool Sept 15%", "Limpeza e desinfecção em única etapa de superfícies onde não se pode fazer enxágue."),
     ]),

    # ============================================================
    # 15. LAVANDERIA
    # ============================================================
    ("Lavanderia",
     "Produtos líquidos ou em pó para limpeza e desinfecção de roupas em lavanderias profissionais, hospitalares, industriais e de hotelaria.",
     [
        ("Pluron 7160 Lavanderia", "Lava e desengordura pisos, fogões e exaustores."),
        ("Pluron Top Grill Lavanderia", "Limpeza de fornos, grelhas, chapas e frigideiras."),
        ("Pluron Det Clean", "Lava utensílios, pisos, paredes, latões, tanques, equipamentos, luvas e botas."),
        ("Pluron Detaclor Lavanderia", "Limpeza manual/por espuma de equipamentos e superfícies engorduradas."),
        ("Pluron Soft Premium", "Amaciante com tecnologia em cápsulas que mantém tecidos perfumados e macios por mais tempo."),
        ("Pluron Soft Intense", "Amaciante perfumado para todos os tecidos em lavanderias."),
        ("Pluron 909 LC", "Amaciante com toque suave, para todos os tipos de tecidos."),
        ("Pluron 835 LL", "2 em 1: amacia e acidula roupas de todos os tipos de tecidos."),
        ("Pluron 144 A Sept Lavanderia", "Desinfecção manual/por imersão de equipamentos, pisos e paredes; cloração de água."),
        ("Pluron 444 A", "Desinfecção manual/por imersão de equipamentos, pisos e paredes; cloração de água."),
        ("Pluron 464 A", "Desinfecção manual/por imersão de equipamentos, pisos e paredes; cloração de água."),
        ("Pluron Passe Pronto", "Oferece rapidez e qualidade na hora de passar; deixa agradável perfume."),
        ("Pluron 836 LL", "Alveja e desinfeta roupas brancas e de cores firmes."),
        ("Pluron 461 A", "Alveja e desinfeta roupas brancas e de cores firmes."),
        ("Pluron 920 LL4", "Assepsia, remoção de manchas e alvejamento de roupas."),
        ("Pluron 960 L", "Assepsia, remoção de manchas e alvejamento de roupas."),
        ("Pluron Maxclor", "Alveja/desinfeta roupas; acidulante e anticloro."),
        ("Pluron 985 L", "Alveja/desinfeta roupas; acidulante e anticloro."),
        ("Pluron 834 LL", "Detergente para lavagem de roupas industriais, hospitalares e de algodão/poliéster."),
        ("Pluron 888 LLO", "Detergente para lavagem de roupas industriais, hospitalares e de algodão/poliéster."),
        ("Pluron Max Detergente em Pó", "Lavagem de roupas de cama, banho e uso pessoal; aditivo alcalino."),
        ("Pluron CIP Lavanderia", "Lavagem de roupas de cama, banho e uso pessoal; aditivo alcalino."),
        ("Pluron 961 L", "Detergente, umectante, acidulante e anticloro para lavagem de roupas."),
        ("Pluron 962 L", "Detergente, umectante, acidulante e anticloro para lavagem de roupas."),
        ("Pluron 949 L", "Detergente, umectante, acidulante e anticloro para lavagem de roupas."),
        ("Pluron Iniby Lav", "Detergente, umectante, acidulante e anticloro para lavagem de roupas."),
        ("Pluron Cloth Wash White", "Lava roupas líquido (sem perfume/corante ou perfumado) para roupas de cama, banho e uso pessoal."),
        ("Pluron Cloth Wash", "Lava roupas líquido (sem perfume/corante ou perfumado) para roupas de cama, banho e uso pessoal."),
        ("Pluron Lava Roupas", "Lavagem e tratamento de manchas de gorduras, óleos, graxas, molhos e batom."),
        ("Pluron Detacid L", "Lavagem e tratamento de manchas de gorduras, óleos, graxas, molhos e batom."),
        ("Pluron Lav Solv", "Lavagem e tratamento de manchas de gorduras, óleos, graxas, molhos e batom."),
        ("Pluron Lav Clean", "Lavagem e tratamento de manchas de gorduras, óleos, graxas, molhos e batom."),
        ("Pluron 833 LL", "Com sequestrantes e dispersantes, evita amarelamento por sais de cálcio e ferro."),
        ("Pluron Alcalav", "Com sequestrantes e dispersantes, evita amarelamento por sais de cálcio e ferro."),
        ("Pluron 911 LLX", "Acidulante, anticloro e removedor de ferrugem; pré-lavagem de sujidade pesada."),
        ("Pluron 837 LL3", "Acidulante, anticloro e removedor de ferrugem; pré-lavagem de sujidade pesada."),
        ("Pluron 847 LLF", "Acidulante, anticloro e removedor de ferrugem; pré-lavagem de sujidade pesada."),
        ("Pluron 964 L", "Acidulante, anticloro e removedor de ferrugem; pré-lavagem de sujidade pesada."),
     ]),

    # ============================================================
    # 16. FARMACÊUTICA E HOSPITALAR
    # ============================================================
    ("Farmacêutica e Hospitalar",
     "Linha completa para o setor farmacêutico e hospitalar, em conformidade com as normas do Ministério da Saúde e ANVISA.",
     [
        ("Pluron 147 BG Sept Saúde", "Álcool 70% com clorexidina, pronto uso, antisséptico das mãos com emoliente."),
        ("Pluron Álcool Foam Saúde", "Antisséptico por espuma, sem necessidade de enxágue."),
        ("Pluron 147 AG Saúde", "Álcool gel 70% antisséptico das mãos."),
        ("Samprox 3,5%", "Esterilização de dialisadores, linhas de hemodiálise e desinfecção de alto nível de máquinas de hemodiálise."),
        ("Samprox 5%", "Esterilização de dialisadores, linhas de hemodiálise e desinfecção de alto nível de máquinas de hemodiálise."),
        ("Pluron Quater LH", "Desinfetante à base de Quaternário de 5ª geração e Biguanida para superfícies fixas e artigos não críticos; ação virucida testada pela UNICAMP."),
     ]),

    # ============================================================
    # 17. AUTOMOTIVA
    # ============================================================
    ("Automotiva",
     "Linha automotiva: limpeza de chassis, carrocerias, motores e rodas até conservação geral de veículos.",
     [
        ("Mustang Silicone Gel", "Renova e revitaliza superfícies de borracha, vinil e plásticos do veículo."),
        ("Mustang Prima", "Renova superfícies emborrachadas como pneus e tapetes; aparência de novo."),
        ("Pluron 7060 M Automotiva", "Sabonete para limpeza de graxas e óleos das mãos em oficinas."),
        ("Solumol 960 R", "Detergente para embelezamento automotivo; realça o brilho da pintura."),
        ("Supermix CR", "Lavagem manual ou automática de veículos e equipamentos com superfícies pintadas."),
        ("Mustang Azulão", "Limpeza super pesada para carrocerias de madeira, alumínio, chassis e motores."),
        ("Pollyclean E", "Limpeza de chassis, motores, rodas, caminhões com carroceria de madeira, baú e tanques pintados."),
        ("Supremix AT", "Limpeza de pisos, equipamentos de inox e alumínio, pátios de manobra e frotas."),
        ("Mustang Solumax DR 8", "Detergente desengraxante concentrado para limpeza impecável; remove graxas e resíduos betuminosos."),
        ("Pluron 7225 Automotiva", "Limpeza de chassis, motores, rodas e caminhões."),
     ]),

    # ============================================================
    # 18. ACESSÓRIOS DE LIMPEZA
    # ============================================================
    ("Acessórios de Limpeza",
     "Materiais operacionais em Polipropileno, alumínio, microfibra e aço para rotinas profissionais.",
     [
        ("Espátula", "Limpador para box, janelas, frestas e fendas; cabo anatômico, acompanha 2 refis de microfibra."),
        ("Pá Coletora", "Com tampa e cabo de alumínio; trava na tampa para descarte seguro."),
        ("Pano de Microfibra", "Alta absorção; elimina poeira, sujeira e graxa, sem arranhar nem soltar fiapos."),
        ("Tela para Mictório", "Tela odorizadora com furos anti-respingos; fragrâncias Fruit-Fruit, Canela, Citrus e Algas."),
        ("Organizador para Cabos", "Mantém os cabos presos e otimiza o espaço; kits com 3, 4 e 6 suportes."),
        ("Placas Sinalizadoras", "Sinalizam e interditam áreas (piso molhado, cuidado, área em manutenção); material PEAD."),
        ("Pulverizador 500 ml", "Uso profissional, alta resistência química, gatilho ajustável para controle do jato."),
        ("Pulverizador 1 L", "Uso profissional, alta resistência química, gatilho ajustável para controle do jato."),
        ("Balde 3 L", "Para limpeza geral e separação de resíduos; material Polipropileno + ABS."),
        ("Balde 6 L", "Para limpeza geral e separação de resíduos; material Polipropileno + ABS."),
        ("Balde 15 L Reforçado", "Graduação interna e bico dosador; produto 2 em 1 (balde + placa sinalizadora)."),
        ("Balde com Espremedor", "Espremedor super resistente com cabo de alumínio e manopla ergonômica."),
        ("Balde Due 30 L", "Divisão interna fixa com graduação; design arredondado e vibrante."),
        ("Rodízios (reposição)", "Para baldes e contentores."),
        ("Caixa Dobrável", "Montagem fácil com sistema de travamento no fundo; suporta 50 kg."),
        ("Cabos e Extensores", "Cabos telescópicos de 3M, 4,5M, 6M e 9M; cabo extensor de 1,40 m."),
        ("Lixeira 12 L Click", "Modelo Click (com tampa), com suporte para bobina de saco."),
        ("Lixeira 12 L Push", "Modelo Push (sem tampa), com suporte para bobina de saco."),
        ("Lixeira 15 L Porta Saco", "3 modelos: sem aro, com aro e aro + tampa."),
        ("Lixeira TVV 60 L", "Tampa basculante de ampla abertura, com durabilidade e estabilidade."),
        ("Lixeira com Pedal 18 L", "Alta resistência, abertura máxima de 75°."),
        ("Lixeira com Pedal 36 L", "Alta resistência, abertura máxima de 75°."),
        ("Lixeira com Pedal 50 L", "Alta resistência, abertura máxima de 75°."),
        ("Lixeira 100 L", "Opção com rodas, alça de deslocamento e abertura de 85°."),
        ("Contentor 120 L", "Com rodas, ideal para coleta urbana, lixo hospitalar e resíduos industriais."),
        ("Contentor 240 L", "Duas rodas de 200 mm e design ergonômico."),
        ("Rodo de Borracha 35 cm", "Borracha dupla expandida de alta absorção."),
        ("Rodo de Borracha 45 cm", "Borracha dupla expandida de alta absorção."),
        ("Rodo de Borracha 55 cm", "Borracha dupla expandida de alta absorção."),
        ("Rodo de Borracha 65 cm", "Borracha dupla expandida de alta absorção."),
        ("Suporte para Mop Pó", "Com hastes metálicas flexíveis, ideal com cabo de 140 cm."),
        ("Suporte para Mop Úmido", "Haste em formato de presilha, com fixação por rosca euro."),
        ("Suporte para Fibra", "Articulação que facilita a limpeza em locais de difícil acesso."),
        ("Refil para Mops", "Para mop úmido ou mop pó, em material de qualidade."),
        ("Suporte de Fibra Manual com Alça", "Pega-mão anatômico para segurança em chapas quentes."),
        ("Kit para Limpeza Titan", "10 itens: carro funcional titan com tampa, balde espremedor Due, placa sinalizadora, suportes de mop, cabos extensores, refis e pá coletora."),
        ("Kit Carro Funcional Pratic", "Balde Due + placa sinalizadora + carro funcional + suporte de mop + cabo + refil."),
        ("Kit Balde Due", "Balde Due + placa sinalizadora + suporte de mop úmido + cabo + refil."),
        ("Kit para Limpeza Completa / Kit Limpa Tudo", "Cabos, suportes e refis para limpeza diária e geral."),
        ("Kit Mopinho", "Balde 15 L sinalizador + refil mopinho 170 g + espremedor."),
        ("Kit Mop Úmido Completo", "Suporte mop úmido + refil ponta dobrada + cabo extensor 1,40 m."),
     ]),
]

class Command(BaseCommand):
    help = "Popula o catálogo HES com todos os tópicos e produtos do catálogo."

    def add_arguments(self, parser):
        parser.add_argument(
            "--reset",
            action="store_true",
            help="Apaga categorias, subcategorias e produtos antes de recriar.",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        if options["reset"]:
            Produto.objects.all().delete()
            Subcategoria.objects.all().delete()
            Categoria.objects.all().delete()
            self.stdout.write(self.style.WARNING("Catálogo anterior apagado."))

        total = 0
        resumo = []

        for cat_nome, cat_desc, produtos in CATALOGO:
            categoria, _ = Categoria.objects.get_or_create(
                nome=cat_nome,
                defaults={"descricao": cat_desc, "ativo": True},
            )
            # Atualiza a descrição da categoria mesmo se ela já existia
            if not _ and categoria.descricao != cat_desc:
                categoria.descricao = cat_desc
                categoria.save(update_fields=["descricao"])

            # Subcategoria padrão "Geral" (o Produto exige uma subcategoria)
            sub, _ = Subcategoria.objects.get_or_create(
                nome="Geral",
                categoria=categoria,
                defaults={"ativo": True, "ordem": 0},
            )

            for produto_nome, produto_desc in produtos:
                obj, criado = Produto.objects.get_or_create(
                    nome=produto_nome,
                    subcategoria=sub,
                    defaults={
                        "descricao": produto_desc,
                        "codigo": "",
                        "ativo": True,
                        "destaque": False,
                    },
                )
                # Atualiza a descrição do produto mesmo se ele já existia
                if not criado and obj.descricao != produto_desc:
                    obj.descricao = produto_desc
                    obj.save(update_fields=["descricao"])
                total += 1

            resumo.append((cat_nome, len(produtos)))

        self.stdout.write(self.style.SUCCESS(
            f"Seed concluído: {len(CATALOGO)} categorias e {total} produtos."
        ))
        for nome, qtd in resumo:
            self.stdout.write(f"  - {nome}: {qtd} produtos")