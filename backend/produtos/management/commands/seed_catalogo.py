# -*- coding: utf-8 -*-
"""
Seed completo do catálogo HES Hygiene Solutions.

Cria TODOS os tópicos do catálogo como Categorias e TODOS os produtos de cada
tópico. Um mesmo produto pode aparecer em mais de um tópico (ex: PLURON 7160
está em Desincrustantes e em Supermercados) - por isso a busca usa
(nome + subcategoria), e não só o nome.

Uso:
    python manage.py seed_catalogo            # cria/atualiza sem duplicar
    python manage.py seed_catalogo --reset    # APAGA categorias/produtos e recria
"""
from django.core.management.base import BaseCommand
from django.db import transaction
from produtos.models import Categoria, Subcategoria, Produto

CATALOGO = [
    # ================= DISPENSERS =================
    ("Linha Gold",
     "Linha premium de dispensers com design sofisticado, alta durabilidade, praticidade, higiene e elegância para ambientes profissionais e corporativos.",
     [
        ("Dispenser Sabonete Espuma DSE05", "Dispenser de sabonete em espuma. Banheiros de empresas, escritórios, shoppings e ambientes corporativos."),
        ("Dispenser Sabonete Líquido DSE10", "Dispenser de sabonete líquido. Banheiros institucionais e corporativos."),
        ("Dispenser Papel Toalha Bobina DPB6300", "Dispenser de papel toalha bobina. Sanitários de alto fluxo: empresas, shoppings, escolas e hospitais."),
        ("Dispenser Papel Toalha Interfolhado DPI2400", "Dispenser de papel toalha interfolhado. Banheiros de empresas, clínicas e ambientes corporativos."),
        ("Dispenser Papel Toalha Interfolhado Mini DPIM1400", "Dispenser de papel toalha interfolhado mini. Sanitários de baixo fluxo ou espaços reduzidos."),
        ("Dispenser Coletor de Absorvente DCA1000", "Coletor de absorventes descartáveis. Banheiros femininos de empresas, shoppings e escolas."),
        ("Dispenser Assento Sanitário DCS1000", "Dispenser de assento sanitário descartável. Higiene extra em banheiros públicos e institucionais."),
        ("Dispenser Guardanapeira Interfolhada DG8000", "Guardanapeira interfolhada. Cozinhas, copas, refeitórios e praças de alimentação."),
        ("Dispenser Papel Higiênico DHI8000", "Dispenser de papel higiênico interfolhado. Banheiros institucionais e de alto tráfego."),
        ("Dispenser Papel Higiênico Bobina DPHB8200", "Dispenser de papel higiênico bobina 8 pol. Sanitários de empresas, escolas e hospitais."),
        ("Dispenser Papel Higiênico Bobina DPHB1620", "Dispenser de papel higiênico bobina 16 pol (duplo). Banheiros de alto fluxo e uso institucional."),
     ]),

    ("Linha Care",
     "Linha Care de dispensers com design suave e funcional, oferecendo segurança, higiene e praticidade ideais para hospitais, clínicas e ambientes institucionais.",
     [
        ("Dispenser Sabonete Espuma DPH-107", "Dispenser de sabonete em espuma. Higiene segura para hospitais, clínicas e laboratórios."),
        ("Dispenser Sabonete Líquido DPH-108", "Dispenser de sabonete líquido. Banheiros de hospitais, clínicas e ambientes de saúde."),
        ("Dispenser Papel Toalha Bobina DPH-101", "Dispenser de papel toalha bobina. Hospitais, clínicas e ambientes institucionais."),
        ("Dispenser Papel Toalha Interfolhado DPH-102", "Dispenser de papel toalha interfolhado. Hospitais, clínicas e instituições de saúde."),
        ("Dispenser Papel Toalha Interfolhado Mini DPH-103", "Dispenser de papel toalha interfolhado mini. Compacto, para clínicas, consultórios e áreas de saúde."),
        ("Dispenser Papel Higiênico DPH-104", "Dispenser de papel higiênico. Sanitários de hospitais, clínicas e instituições."),
        ("Dispenser Papel Higiênico DPH-105", "Dispenser de papel higiênico com capacidade extra. Alto fluxo em ambientes de saúde."),
        ("Dispenser Papel Higiênico DPH-106", "Dispenser de papel higiênico. Banheiros de hospitais e clínicas."),
        ("Dispenser Coletor de Absorvente DPH-109", "Coletor de absorventes descartáveis. Banheiros de hospitais, clínicas e empresas."),
        ("Dispenser Assento Sanitário DPH-110", "Dispenser de assento sanitário descartável. Higiene em sanitários de hospitais e clínicas."),
        ("Dispenser Guardanapeira Interfolhada DPH-111", "Guardanapeira interfolhada. Refeitórios e copas de hospitais e instituições."),
     ]),

    ("Linha Standard",
     "Linha Standard de dispensers: funcionalidade, durabilidade e praticidade em design versátil, proporcionando higiene, segurança e economia.",
     [
        ("Dispenser Sabonete Líquido ELT-2105", "Dispenser de sabonete líquido versátil. Banheiros de empresas, comércio e estabelecimentos em geral."),
        ("Dispenser Sabonete Espuma ELT-2106", "Dispenser de sabonete em espuma. Higiene econômica para banheiros institucionais e comerciais."),
        ("Dispenser Papel Toalha Bobina ELT-2101", "Dispenser de papel toalha bobina. Banheiros de empresas, comércios e escolas."),
        ("Dispenser Papel Toalha Interfolhado ELT-2102", "Dispenser de papel toalha interfolhado. Sanitários comerciais e institucionais."),
        ("Dispenser Papel Toalha Interfolhado Mini ELT-2103", "Dispenser de papel toalha interfolhado mini. Compacto para comércios e espaços reduzidos."),
        ("Dispenser Coletor de Absorvente ELT-2107", "Coletor de absorventes descartáveis. Banheiros femininos de empresas e comércios."),
        ("Dispenser Assento Sanitário ELT-2108", "Dispenser de assento sanitário descartável. Banheiros públicos e comerciais."),
        ("Dispenser Guardanapeira Interfolhada ELT-2109", "Guardanapeira para copas, cozinhas e refeitórios comerciais."),
        ("Dispenser Papel Higiênico ELT-2104", "Dispenser de papel higiênico. Banheiros comerciais e institucionais."),
     ]),

    # ================= EQUIPAMENTOS =================
    ("Equipamentos Profissionais",
     "Equipamentos desenvolvidos para alto desempenho, segurança e eficiência em ambientes industriais, comerciais e de serviços.",
     [
        ("Diluidor de Produtos Químicos (Sistema Venturi)", "Sistema de diluição de produtos concentrados por Venturi, com diluições precisas via TIP. Fornecimento e instalação. Uso em cozinhas industriais, hospitais e indústrias."),
        ("Dosador para Máquinas de Lavar Louça", "Dosador individual para higienização em máquinas de lavar louça. Cozinhas de restaurantes, hotéis e indústrias."),
        ("Dosador para Lavanderia", "Dosador individual para processos de lavanderia profissional. Lavanderias hospitalares, industriais e de hotelaria."),
        ("Treinamento de Utilização e Segurança", "Treinamento completo para uso correto e seguro de produtos e equipamentos de limpeza profissional."),
     ]),

    # ================= PAPÉIS =================
    ("Papéis Institucionais",
     "Linha de papéis institucionais com alta absorção, resistência e suavidade, garantindo durabilidade, higiene e conforto em cada uso.",
     [
        ("Toalha Papel Bobina 200M PTB8200", "Papel toalha bobina 200m (6x200m). Alta absorção e resistência para sanitários de alto fluxo."),
        ("Toalha Papel Bobina 150M PTB8150", "Papel toalha bobina 150m (6x150m). Sanitários institucionais e comerciais."),
        ("Papel Higiênico Bobina Folha Dupla PHBD8300", "Papel higiênico bobina folha dupla, 10cm x 300m (8 rolos/caixa). Maciez e resistência."),
        ("Papel Higiênico Bobina Folha Simples PHB8300", "Papel higiênico bobina folha simples, 10cm x 300m. Econômico para uso institucional."),
        ("Papel Higiênico Interfolhado Folha Dupla IHI12", "Papel higiênico interfolhado folha dupla, 20x21cm, pacote 1000 folhas. Para dispensers interfolhados."),
        ("Papel Higiênico Interfolhado Folha Dupla PHCLFD20X10/8000", "Papel higiênico interfolhado folha dupla, 20x10cm, 8.000 folhas/caixa. Alto fluxo."),
        ("Toalha Interfolhada 2 Dobras PTI1250", "Papel toalha interfolhado 2 dobras, 10x21cm, 8.000 folhas/caixa. Higiene sem contato."),
        ("Toalha Interfolhada 3 Dobras PTI12400", "Papel toalha interfolhado 3 dobras, 22x23cm, 2.400/12.000 folhas. Dispensers interfolhados profissionais."),
     ]),

    # ================= HIGIENE PESSOAL =================
    ("Higiene Pessoal",
     "Linha completa de sabonetes líquidos, espuma, antissépticos e álcool em gel para higienização das mãos em escolas, hotéis, hospitais e indústrias.",
     [
        ("PLURON CLOREXIDINE", "Sabonete/antisséptico de mãos à base de clorexidina. Limpeza e higienização das mãos e corpo, com glicerina que evita o ressecamento da pele."),
        ("PLURON HANDMAX ERVA DOCE", "Sabonete perfumado para aplicação por espuma e/ou spray. Limpeza das mãos em empresas, hotéis, clínicas e indústrias."),
        ("PLURON HANDMAX BLUE", "Sabonete líquido perfume floral. Fórmula concentrada que proporciona lavagem eficiente com pequena quantidade."),
        ("PLURON HANDFOAM", "Sabonete perfumado de aplicação por espuma. Versões Cereja e Avelã, Pêssego e Erva Doce."),
        ("PLURON 144 A SEPT", "Sabonete com triclosan na formulação, promovendo proteção e inibição de microrganismos na pele. Limpeza e assepsia das mãos."),
        ("PLURON 7060 M", "Sabonete para limpeza de graxas e óleos das mãos. Oficinas mecânicas e indústrias."),
        ("PLURON FOAM HAND SEPT", "Sabonete espuma antisséptico para limpeza e assepsia das mãos. Formulação específica para dispensers de espuma; indústrias alimentícias."),
        ("PLURON 147 AG", "Álcool gel 70% antisséptico das mãos. Pronto uso, com emoliente. Testado contra S. choleraesuis, E. coli, S. aureus e P. aeruginosa."),
        ("PLURON 147 BG SEPT", "Álcool 70% com clorexidina para assepsia das mãos. Aplicável em saboneteiras spray."),
        ("PLURON ÁLCOOL FOAM", "Álcool antisséptico em espuma, sem necessidade de enxágue. Com emoliente que evita o ressecamento."),
     ]),

    # ================= TRATAMENTO DE PISO =================
    ("Tratamento de Piso",
     "Produtos para limpeza, remoção de ceras, selamento e brilho de pisos laváveis: mármore, cerâmica, porcelanato, Paviflex, granilite e outros.",
     [
        ("PLURON 7215", "Limpeza de pisos de mármore, borracha, cerâmica e plásticos através de lavadoras automáticas."),
        ("PLURON 7225", "Remoção de ceras de pisos porosos (exceto madeira), sujidades de terra em pisos encardidos e gorduras de superfícies, pisos e paredes."),
        ("PLURON 7230", "Limpeza de pisos, paredes, equipamentos e caixas plásticas em indústrias. Fórmula concentrada que penetra rapidamente nas sujidades."),
        ("PLURON TOP REMOVE", "Remoção de ceras e sujidades em Paviflex, Plurigoma, Ardósia, Pedras Naturais, Granilite e Mármore (exceto madeira)."),
        ("PLURON SELAFIX", "Base seladora antiderrapante para área interna. Resistência ao tráfego e excelente desempenho em diversos tipos de piso."),
        ("PLURON SELAFIX EX", "Base seladora para área interna e externa. Não inflamável, resistente ao tráfego; restaura pisos laváveis com equipamentos HS e UHS."),
        ("PLURON MAXBRILHO AT", "Cera auto brilho e impermeabilizante para pisos laváveis. Dispensa enceradeira, é antiderrapante e resistente ao tráfego."),
        ("PLURON TOP BRILHO", "Cera auto brilho 3x1: sela, dá brilho e protege. Polímeros de alta tecnologia com efeito antiderrapante."),
        ("PLURON 7914", "Cera auto brilho para pisos laváveis. Dispensa enceradeira, antiderrapante e resistente ao tráfego."),
     ]),

    # ================= LIMPADORES / ODORIZANTES =================
    ("Limpadores Perfumados e Odorizantes",
     "Limpadores de uso geral, perfumados e odorizantes para pisos, vidros, superfícies e ambientes.",
     [
        ("PLURON TRIOXY", "Concentrado à base de peróxido de hidrogênio e tensoativos. Limpeza geral e alvejamento de superfícies, inclusive sujidades de mofo."),
        ("PLURON 7470", "Limpeza diária de vidros, espelhos, acrílicos, azulejos, fórmica, telefones e superfícies de plásticos, metais e courvin."),
        ("PLURON LIMPADOR CAPIM LIMÃO", "Limpeza manual de pisos laváveis e superfícies de residências, hospitais, condomínios, shoppings e escolas. Perfume agradável."),
        ("PLURON LIMPADOR PITANGA", "Limpeza manual de pisos e superfícies em ambientes institucionais e comerciais, com perfume agradável."),
        ("PLURON MULTI CITRONELA", "Multiuso com citronela, afastando insetos como moscas, mosquitos e pernilongos."),
        ("PLURON MULTI PORCELANATO", "Produto de baixa espumação para limpeza de pisos de porcelanato e outros tipos de piso."),
        ("PLURON H8 PREMIUM", "Elimina o cheiro de tabaco e atua como odorizante de ambiente. Aplicável em clínicas e estabelecimentos comerciais."),
        ("PLURON H3 HERBAL", "Limpeza de pisos de mármore, borracha, cerâmica e plásticos através de mop ou lavadoras automáticas."),
        ("PLURON H4 MARINE", "Limpeza manual de pisos e superfícies impregnadas com gorduras ou sujidades de natureza arenosa."),
        ("PLURON H5 PREMIUM", "Detergente perfumado para limpeza pesada de pisos e superfícies impregnadas com gorduras."),
        ("PLURON H4 PREMIUM", "Limpeza manual de pisos e superfícies impregnadas com gorduras ou sujidades arenosas. Uso em hospitais, condomínios, shoppings e escolas."),
     ]),

    # ================= DESINFETANTES =================
    ("Desinfetantes Perfumados",
     "Desinfetantes com ação bactericida e perfume agradável para pisos e superfícies em geral.",
     [
        ("PLURON SANIT EUCALIPTO", "Desinfetante perfumado eucalipto com ação bactericida contra Staphylococcus aureus e Salmonella choleraesuis."),
        ("PLURON SANIT FLORAL", "Desinfetante bactericida contra S. aureus e S. choleraesuis. Pisos e superfícies em geral."),
        ("PLURON SANIT FLORAL FRESH", "Desinfetante bactericida com perfume floral fresh."),
        ("PLURON SANIT INTENSE FLORAL", "Desinfetante bactericida com fragrância floral intensa."),
        ("PLURON SANIT INTENSE SUMMER", "Desinfetante perfumado com fragrância intensa. Desinfecção de pisos e superfícies."),
        ("PLURON SANIT INTENSE MARINE", "Desinfetante perfumado com fragrância marine intensa."),
        ("PLURON SANIT LAVANDA", "Desinfetante perfumado lavanda com ação bactericida contra S. aureus e S. choleraesuis."),
        ("PLURON SANIT MARINE", "Desinfetante perfumado marine com ação bactericida."),
        ("PLURON SANIT TOP FLORAL", "Desinfetante bactericida que desinfeta, limpa e odoriza o ambiente."),
        ("PLURON SANIT TOP LAVANDA", "Desinfetante à base de quaternário de amônio, eficaz contra Coronavírus (SARS-CoV-2/COVID19, MERS e outros)."),
     ]),

    ("Detergentes Perfumados",
     "Detergentes perfumados para limpeza de equipamentos, superfícies, vasos sanitários e ambientes em geral.",
     [
        ("POLLYCLEAN 10.000", "Detergente flotador para limpeza de equipamentos de cozinhas, pias, fogão, fórmicas, plásticos, banheiros, pisos, azulejos, balcões, cerâmica e mármore."),
        ("PLURON H2 PREMIUM", "Limpador de vasos sanitários que remove manchas de sais (cálcio, magnésio e ferro), evita manchas e não possui ácido fluorídrico. Seguro para louças sanitárias."),
     ]),

    # ================= DESINCRUSTANTES =================
    ("Desincrustantes e Limpa Alumínio",
     "Produtos para desincrustação de gorduras carbonizadas e limpeza de utensílios de alumínio.",
     [
        ("PLURON 7160", "Lava e desengordura pisos, fogões, exaustores, pias, azulejos, geladeiras e banheiros. Fórmula concentrada."),
        ("PLURON 7710 AE", "Limpeza por espuma de equipamentos, pisos e superfícies impregnadas com gorduras carbonizadas e resíduos oleosos em indústrias alimentícias."),
        ("PLURON LA 21", "Detergente de característica ácida para limpeza e brilho de utensílios de alumínio."),
        ("PLURON 7756", "Higienização de pratos, talheres, bandejas, copos, xícaras e utensílios em máquinas de lavar de cozinhas de hotéis, hospitais, shoppings e escolas."),
        ("PLURON VERSAT", "Limpeza de depósitos de gorduras carbonizadas em utensílios de alumínio (panelas, coifas, frigideiras, assadeiras, latões, tanques, fogões industriais, filtros de coifas e chapas). Também em banho de guarda de formas de queijo."),
     ]),

    # ================= COZINHA INDUSTRIAL =================
    ("Cozinha Industrial e Restaurantes",
     "Linha formulada para as demandas rigorosas de cozinhas industriais, bares, restaurantes, padarias e açougues.",
     [
        ("PLURON TOP GRILL", "Limpeza de fornos, grelhas, chapas, frigideiras e superfícies com gordura carbonizada. Tensoativo espumante que adere à superfície."),
        ("PLURON 236 A", "Limpeza e desincrustação de formas, latões, caixas plásticas, garrafas, louças, ordenhadeiras mecânicas e recipientes. Também para legumes, frutas e verduras."),
        ("PLURON 7888", "Desinfetante para frutas, legumes e verduras. Ação biocida contra Enterococcus Faecium e Escherichia coli (ANVISA). Não usar em cobre e alumínio."),
        ("PLURON 7799 A", "Enxágue final de máquinas de lavar louças: secagem rápida e eliminação de manchas."),
        ("PLURON MAQ DUO", "Produto 2x1 para lavagem e secagem de louças em máquinas de lavar louças."),
        ("PLURON MAQ DET", "Detergente para pratos, talheres, bandejas, copos e xícaras em máquinas de lavar. Também para caixas plásticas."),
        ("PLURON MAQ SEC", "Enxágue final de máquinas de lavar louças para secagem rápida e eliminação de manchas."),
        ("PLURON MAQ CLOR", "Limpeza de pratos, talheres, bandejas, copos e xícaras em máquinas de lavar. Não usar em cobre e alumínio."),
        ("PLURON 194 A", "Lava utensílios de cozinha, pisos, paredes, latões, tanques, mesas de trabalho, caminhões-tanque e equipamentos. Elimina sujidades e gorduras."),
        ("PLURON 194 AV", "Lava utensílios de cozinha, pisos, paredes, latões, tanques, mesas de trabalho, caminhões-tanque e equipamentos."),
        ("PLURON 404 A", "Lava utensílios, louças, pisos, paredes, latões, tanques e equipamentos em indústrias alimentícias, farmacêuticas e cozinhas industriais."),
        ("PLURON 406 A", "Limpeza manual de pisos, paredes, latões, tanques, equipamentos, louças e utensílios em indústrias alimentícias e cozinhas industriais."),
        ("PLURON DETERGENTE NEUTRO", "Lava utensílios de cozinha, pisos, paredes, latões, tanques e equipamentos. Reduz a tensão superficial, facilitando a remoção da gordura."),
     ]),

    # ================= LATICÍNIOS =================
    ("Laticínios",
     "Produtos específicos para limpeza e desinfecção de toda a cadeia do leite: ordenha, tanques de transporte, armazenamento e pasteurizadores.",
     [
        ("PLURON ALCALI CLOR", "Baixa espuma. Limpeza de ordenhadeiras mecânicas, tanques de recepção, estocagem, misturadores, resfriadores, equipamentos e tubulações."),
        ("PLURON CLORCIP", "Baixa espuma. Limpeza CIP de ordenhadeiras, pisos, paredes, equipamentos e garrafões. Também circuitos post mix, chopeiras e máquinas de lavar pratos."),
        ("PLURON 426 A", "Uso manual e por circulação. Limpeza de pisos, paredes, latões, tanques de recepção, resfriadores, tanques de estocagem e equipamentos."),
        ("PLURON 327 AS", "Limpeza por circulação (CIP) de tanques, equipamentos, tubulações, pasteurizadores, evaporadores, resfriadores, ordenhadeiras e garrafas de vidro."),
        ("PLURON 327 CIP", "Limpeza por circulação de pasteurizadores, evaporadores, resfriadores, ordenhadeiras e tubulação de aço inox. Também gordura carbonizada em fornos, grelhas e fritadeiras."),
        ("PLURON NITRIC", "Ácido de baixa espuma para limpeza por circulação de pasteurizadores, evaporadores e ordenhadeiras. Remove resíduos minerais, pedras de leite e calcificações."),
        ("PLURON 320 A", "Limpeza ácida de tanques de fermentação e maturação de cerveja, tubulações, pasteurizadores e ganchos. Também fosfatização de superfícies metálicas."),
        ("PLURON 418 A", "Limpeza por espuma de superfícies impregnadas com gorduras e resíduos de óleos em indústrias alimentícias e de bebidas."),
        ("PLURON 446 A", "Limpeza de pisos, azulejos de cozinhas e equipamentos em geral. Não causa corrosão em plásticos, alumínio, cobre e metais galvanizados."),
        ("PLURON 489 AT5", "Limpeza manual ou por espuma de equipamentos, pisos, paredes e superfícies com gorduras e resíduos oleosos."),
        ("PLURON 428 A4", "Limpeza por espuma de superfícies impregnadas com gorduras e resíduos oleosos em indústrias alimentícias, cozinhas, restaurantes e hospitais."),
        ("PLURON 447 AE", "Limpeza por espuma e manual de superfícies com gorduras, proteínas e resíduos de óleos. Também pisos, paredes, latões, tanques, equipamentos e banheiros."),
        ("PLURON 489 A", "Limpeza manual ou por espuma de equipamentos, pisos, paredes e superfícies impregnadas com gorduras e resíduos oleosos."),
        ("PLURON 490 A", "Remoção de sujidades inorgânicas em ambientes exclusivamente industriais. Indústrias de alimentos, frigoríficos, farmacêuticas e bebidas."),
        ("PLURON 490 AM", "Remoção de sujidades inorgânicas em ambientes exclusivamente industriais."),
        ("PLURON ACID FOAM", "Detergente ácido para limpeza externa em indústrias alimentícias, farmacêuticas e cosméticos. Remove pedra cervejeira e pedra de leite. Enchedoras e esteiras."),
        ("PLURON 786 B5", "Aditivo para soluções cáusticas na lavagem de garrafas e nos sistemas CIP. Reduz a frequência da limpeza ácida."),
        ("PLURON CE 800 B", "Aditivo na lavagem de garrafas e máquinas em geral. Também utilizado como antiespumante."),
        ("PLURON 950 PACK", "Limpa e lubrifica esteiras e correntes de transporte de embalagens cartonadas."),
        ("PLURON 461 A1", "Desinfecção de equipamentos, ordenhadeiras, tanques de estocagem, válvulas, tubulações, pisos e paredes. Baixa formação de espuma."),
        ("PLURON 463 AP", "Desinfecção de superfícies, tanques de estocagem, válvulas, tubulações, pisos e paredes em indústrias alimentícias e em geral."),
        ("PLURON 444 A", "Desinfecção manual por imersão ou circulação de equipamentos, tanques, válvulas, tubulações, pisos e paredes. Também cloração de água e hortifrutícolas."),
        ("PLURON HIDROXYSEPT", "Desinfecção de equipamentos, tanques de estocagem, válvulas, tubulações, pisos e paredes em indústrias de alimentos."),
        ("PLURON 464 A", "Desinfecção de instalações, equipamentos, superfícies, pisos e utensílios. Elimina odores e age contra bactérias, bolores e leveduras."),
        ("PLURON TS 787 B", "Limpeza por circulação nas linhas de troca de sabores e nos circuitos de post-mix nas indústrias de bebidas. Tensoativo de baixa espuma."),
        ("PLURON 484 A", "Limpeza manual de pisos, paredes, latões, tanques, equipamentos e caminhões-tanque em indústrias alimentícias e farmacêuticas."),
        ("PLURON 485 A", "Lava utensílios, pisos, paredes, latões, tanques, equipamentos, botas e luvas."),
        ("PLURON 485 A SE", "Lava utensílios, pisos, latões, tanques, equipamentos e utensílios em indústrias farmacêuticas e em geral."),
        ("PLURON 485 AE", "Limpeza de pisos, paredes, caminhões-tanque, equipamentos, luvas e botas em indústrias alimentícias, farmacêuticas, hospitais, escolas e clínicas."),
     ]),

    # ================= CARRETILHAS =================
    ("Tratamento de Carretilhas, Trilhos e Nóreas",
     "Produtos para limpeza e proteção de ganchos, carretilhas, trilhos e nóreas de ferro e aço.",
     [
        ("PLURON 199 A1", "Utilizado por imersão para proteção de ganchos e carretilhas de ferro e aço contra oxidação. Também fosfatização de superfícies metálicas."),
        ("PLURON 199 A2", "Limpeza e proteção por imersão de ganchos e carretilhas de ferro ou aço contra oxidação."),
        ("PLURON 337 AB", "Limpeza de ganchos, carretilhas e garrafas e limpeza por circulação de pasteurizadores, evaporadores, resfriadores e tubulação de aço inox."),
        ("PLURON 488 A", "Limpeza por imersão de cozinhadores contínuos ou estáticos, ganchos e carretilhas. Remove gorduras carbonizadas e incrustações da água."),
     ]),

    # ================= FRIGORÍFICOS =================
    ("Frigoríficos e Abatedouros",
     "Linha desenvolvida para atender às normas de higiene dos Ministérios da Saúde e da Agricultura em frigoríficos e abatedouros.",
     [
        ("PLURON CLOROFOAM AL", "Limpeza por espuma de superfícies impregnadas com gorduras e resíduos oleosos. Possui cloro que auxilia na limpeza e sanitização."),
        ("PLURON DETACLOR", "Limpeza manual ou por espuma de equipamentos, pisos, paredes e superfícies com gorduras e resíduos oleosos. Cloro auxilia na sanitização."),
        ("PLURON 485 A", "Lava utensílios, pisos, paredes, latões, tanques, equipamentos, botas e luvas em indústrias alimentícias e frigoríficos."),
        ("PLURON 485 A SE", "Lava utensílios, pisos, latões, tanques e equipamentos. Uso em frigoríficos e indústrias farmacêuticas."),
        ("PLURON 485 AE", "Limpeza de pisos, paredes, caminhões-tanque, equipamentos, luvas e botas em frigoríficos e indústrias em geral."),
        ("PLURON 484 A", "Limpeza manual de pisos, paredes, latões, tanques, equipamentos e caminhões-tanque em frigoríficos e indústrias."),
        ("PLURON 404 A", "Lava utensílios, louças, pisos, paredes, latões, tanques e equipamentos. Indicado em frigoríficos e indústrias alimentícias."),
        ("PLURON 406 A", "Limpeza manual de pisos, paredes, latões, tanques, equipamentos, louças e utensílios em frigoríficos e indústrias."),
        ("PLURON 7230", "Limpeza de pisos, paredes, equipamentos e caixas plásticas em frigoríficos e indústrias em geral."),
        ("PLURON 327 AS", "Limpeza por circulação (CIP) de tanques, equipamentos, tubulações, pasteurizadores e ordenhadeiras em frigoríficos."),
        ("PLURON 320 A", "Limpeza ácida de tanques, tubulações e ganchos; também fosfatização de superfícies metálicas em frigoríficos."),
        ("PLURON 327 CIP", "Limpeza por circulação em frigoríficos e indústrias de alimentos; tubulação de aço inox."),
        ("PLURON 194 A", "Lava utensílios, pisos, paredes, latões, tanques, mesas de trabalho e equipamentos em frigoríficos."),
        ("PLURON 194 AV", "Lava utensílios, pisos, paredes, latões, tanques, mesas de trabalho e equipamentos em frigoríficos."),
     ]),

    # ================= SUPERMERCADOS =================
    ("Supermercados",
     "Produtos para limpeza e desinfecção de supermercados, padarias, açougues e áreas de manipulação de alimentos.",
     [
        ("PLURON 7160", "Lava e desengordura pisos, fogões, exaustores, pias, azulejos e banheiros em supermercados e comércios."),
        ("PLURON TOP GRILL", "Limpeza de fornos, grelhas, chapas e frigideiras com gordura carbonizada em padarias, açougues e restaurantes."),
        ("PLURON DET CLEAN", "Lava utensílios, pisos, paredes, latões, tanques, mesas de trabalho, equipamentos, luvas e botas. Limpeza pesada de supermercados."),
        ("PLURON DETACLOR", "Limpeza manual ou por espuma de equipamentos, pisos, paredes e superfícies. Cloro auxilia na limpeza e sanitização."),
        ("PLURON 144 A SEPT", "Sabonete com triclosan, proteção e inibição de microrganismos na pele. Higiene das mãos em supermercados e comércios."),
        ("PLURON 444 A", "Desinfecção manual por imersão ou circulação de equipamentos, pisos e paredes. Também cloração de água e hortifrutícolas."),
        ("PLURON 464 A", "Desinfecção de instalações, equipamentos, superfícies, pisos e utensílios. Elimina odores desagradáveis."),
     ]),

    # ================= LAVANDERIA =================
    ("Lavanderia",
     "Produtos líquidos ou em pó para limpeza e desinfecção de roupas em lavanderias profissionais, hospitalares, industriais e de hotelaria.",
     [
        ("PLURON SOFT PREMIUM", "Amaciante com tecnologia em cápsulas: mantém os tecidos perfumados e macios por muito mais tempo."),
        ("PLURON SOFT INTENSE", "Amaciante perfumado para todos os tipos de tecidos em lavanderias hospitalares, comerciais, industriais e de hotelaria."),
        ("PLURON 909 LC", "Amaciante com toque suave no perfume, para todos os tipos de tecidos em lavanderias profissionais."),
        ("PLURON 835 LL", "Produto 2 em 1: amacia e acidula roupas de todos os tipos de tecidos."),
        ("PLURON PASSE PRONTO", "Para todos os tipos de roupas, oferecendo rapidez e qualidade ao passar e deixando perfume agradável."),
        ("PLURON 836 LL", "Alveja e desinfeta roupas brancas e de cores firmes de algodão e algodão/poliéster. Não causa manchas em presença de clorexidina."),
        ("PLURON 920 LL4", "Assepsia, remoção de manchas e alvejamento de roupas de algodão/poliéster brancas ou coloridas."),
        ("PLURON 960 L", "Alvejante em pó que remove manchas de sangue, frutas, molhos, bebidas e remédios. Não revela manchas de clorexidina."),
        ("PLURON MAXCLOR", "Alveja e desinfeta roupas de algodão e algodão/poliéster. Ação biocida contra S. aureus, Salmonella choleraesuis e Pseudomonas aeruginosa."),
        ("PLURON 985 L", "Acidulante e anticloro na lavagem de roupas brancas ou coloridas. Aumenta a vida útil das peças e diminui irritações na pele."),
        ("PLURON 834 LL", "Lavagem de roupas industriais e hospitalares. Branqueador óptico que deixa as roupas mais brancas."),
        ("PLURON 888 LLO", "Remoção de gorduras, sangue e medicamentos em roupas de algodão e poliéster/algodão. Branqueador óptico realça o brilho."),
        ("PLURON MAX DETERGENTE EM PÓ", "Detergente para roupas de cama, banho e uso pessoal. Eficiente em roupas hospitalares, de hotéis e lavanderias profissionais."),
        ("PLURON CIP LAVANDERIA", "Aditivo alcalino em processos de lavagem de roupas brancas ou coloridas com sujidade média ou pesada. Não agride cores e fibras."),
        ("PLURON 961 L", "Umectação e lavagem de roupas. Pode ser utilizado com um detergente alcalino."),
        ("PLURON 962 L", "Umectação e lavagem de roupas. Apropriado para tecidos delicados como seda, lã, nylon e cobertores."),
        ("PLURON 949 L", "Acidulante e anticloro na lavagem de roupas brancas ou coloridas."),
        ("PLURON INIBY LAV", "Neutraliza resíduos de detergentes clorados (clorexidina) e remove manchas de protetores solares, bronzeadores e lubrificantes."),
        ("PLURON CLOTH WASH WHITE", "Lava roupas líquido sem perfume e sem corante, com alto teor de branqueador óptico. Roupas brancas e coloridas."),
        ("PLURON CLOTH WASH", "Lava roupas líquido perfumado para roupas de cama, banho e uso pessoal. Todos os tipos de tecido."),
        ("PLURON LAVA ROUPAS", "Detergente para todos os tipos de roupas. Alcanolamida de coco evita o ressecamento da pele. Não agride fibras e cores."),
        ("PLURON DETACID L", "Tratamento de roupas manchadas de gorduras, óleos, graxas e batom/maquiagem."),
        ("PLURON LAV SOLV", "Remoção de manchas de gorduras, óleos, molhos e batom. Tensoativo de baixa formação de espuma."),
        ("PLURON LAV CLEAN", "Lava roupas líquido sem perfume e sem corante, para roupas de cama, banho e uso pessoal."),
        ("PLURON 833 LL", "Contém sequestrantes e dispersantes que evitam o amarelamento da roupa por sais de cálcio e ferro."),
        ("PLURON ALCALAV", "Branqueador óptico que deixa as roupas mais brancas e tensoativos biodegradáveis de baixa espuma."),
        ("PLURON 911 LLX", "Usado associado a detergente neutro na lavagem de roupas brancas ou coloridas com sujidade média ou pesada."),
        ("PLURON 837 LL3", "Anticloro e acidulante na lavagem de roupas brancas ou coloridas. Reduz enxágues, tempo e consumo de água. Elimina traças."),
        ("PLURON 847 LLF", "Acidulante e removedor de ferrugem em roupas brancas ou coloridas. Não aplicar em superfícies não resistentes a ácidos."),
        ("PLURON 964 L", "Pré-lavagem e lavagem de roupas com sujidade pesada em lavanderias industriais. Pode ser usado em materiais sintéticos."),
     ]),

    # ================= FARMACÊUTICA / HOSPITALAR =================
    ("Farmacêutica e Hospitalar",
     "Linha completa para o setor farmacêutico e hospitalar, em conformidade com as normas do Ministério da Saúde e ANVISA.",
     [
        ("PLURON 147 BG SEPT SAÚDE", "Álcool 70% com clorexidina, pronto uso, antisséptico das mãos. Testado contra S. aureus, S. choleraesuis, P. aeruginosa e E. coli (laudo ANVISA)."),
        ("PLURON ÁLCOOL FOAM SAÚDE", "Álcool antisséptico em espuma, pronto uso, sem enxágue. Testado contra S. choleraesuis, E. coli, S. aureus e P. aeruginosa."),
        ("PLURON 147 AG SAÚDE", "Álcool em gel 70% antisséptico das mãos à base de álcool etílico. Amplo espectro testado em laboratório credenciado pela ANVISA."),
        ("PLURON QUATER LH", "Desinfetante à base de quaternário de amônio de 5ª geração e biguanida. Superfícies fixas e artigos não críticos em hospitais. Eficaz contra KPC, C. Albicans, Acinetobacter e Coronavírus."),
     ]),

    ("Hemodiálise",
     "Produtos para esterilização e desinfecção de alto nível de máquinas, dialisadores e linhas de hemodiálise.",
     [
        ("SAMPROX 3,5%", "Ácido peracético para esterilização de dialisadores, linhas de hemodiálise e desinfecção de alto nível de máquinas. Embalagem 5L com proteção UV. Proibido uso por imersão."),
        ("SAMPROX 5%", "Esterilização de dialisadores e linhas de hemodiálise e desinfecção de alto nível das máquinas. Laudos ANVISA de eficácia e segurança."),
     ]),

    # ================= AUTOMOTIVA =================
    ("Automotiva",
     "Linha automotiva: limpeza de chassis, carrocerias, motores e rodas até conservação geral de veículos. Ideal para transportadoras, postos, lava-jatos e empresas de ônibus.",
     [
        ("SOLUMOL 960 R", "Detergente para embelezamento automotivo. Realça o brilho da pintura na primeira lavagem."),
        ("SUPERMIX CR", "Lavagem manual ou automática de veículos e equipamentos com superfícies pintadas."),
        ("MUSTANG AZULÃO", "Limpeza super pesada para carrocerias de madeira, alumínio, chassis, motores e sujidades intensas."),
        ("POLLYCLEAN E", "Limpeza de chassis, motores, rodas, caminhões com carrocerias de madeira, baú e tanques pintados."),
        ("SUPREMIX AT", "Limpeza de pisos, equipamentos de inox e alumínio, pátios de manobra e frotas de veículos."),
        ("MUSTANG SOLUMAX DR 8", "Detergente desengraxante concentrado. Elimina sujeiras pesadas: graxas, óleos e resíduos betuminosos. Também chassis, motores, rodas e baús."),
        ("PLURON 7060 M", "Limpeza de graxas e óleos das mãos em oficinas mecânicas e indústrias."),
        ("PLURON 7225", "Eficiente na limpeza de chassis, motores, rodas e caminhões com carrocerias de madeira, baú e tanques pintados."),
     ]),

    ("Recuperadores de Superfícies",
     "Produtos para renovar e revitalizar superfícies de borracha, vinil e plásticos de veículos.",
     [
        ("MUSTANG SILICONE GEL", "Renova e revitaliza superfícies de borracha, vinil e plásticos do veículo. Restaura o brilho original protegendo contra sol e tempo."),
        ("MUSTANG PRIMA", "Renova superfícies emborrachadas como pneus e tapetes de veículos. Aplicação fácil, com aparência de pneus novos."),
     ]),

    # ================= ACESSÓRIOS =================
    ("Acessórios de Limpeza",
     "Acessórios profissionais para rotinas de limpeza: panos, baldes, lixeiras, rodos, mops, pulverizadores, sinalização e kits.",
     [
        ("Espátula", "Limpador para box, janelas, frestas e fendas. Cabo anatômico, super resistente. Acompanha 2 refis de microfibra. Polipropileno."),
        ("Pá Coletora", "Pá coletora com tampa e cabo de alumínio. Trava na tampa mantendo-a aberta para descarte seguro. Polipropileno e microfibra, 600g."),
        ("Limpa Vidros", "Limpador profissional para vidros e superfícies lisas. Cabo anatômico e fácil higienização."),
        ("Pano de Microfibra", "Microfibra de alta absorção. Elimina poeira, sujeira e graxa sem arranhar nem soltar fiapos. Kits com 4, 6 ou 12 unidades."),
        ("Organizador para Cabos", "Organiza equipamentos de limpeza e otimiza o armazenamento. Polipropileno. Kit com 3 a 6 suportes."),
        ("Tela para Mictório", "Tela odorizadora com furos anti respingos, embalada individualmente. Fragrâncias: fruit-fruit, canela, citrus e algas. PVC injetável."),
        ("Placas Sinalizadoras", "Placas para sinalizar e interditar áreas na prevenção de acidentes: cuidado, piso molhado, não entre, área em manutenção. Leves e resistentes."),
        ("Pulverizador 500ml", "Pulverizador profissional de uso contínuo com alta resistência química. Gatilho ajustável. 500ml."),
        ("Pulverizador 1L", "Pulverizador profissional de alta resistência química e durabilidade. Gatilho ajustável. 1 litro."),
        ("Balde 3 Litros", "Balde 3L com graduação interna para diluição correta. Bico dosador na borda. Polipropileno + ABS."),
        ("Balde 6 Litros", "Balde 6L com graduação interna e bico dosador. Limpeza geral e separação de resíduos."),
        ("Balde 15L Reforçado", "Balde 15 litros com alça. Acompanha ou recebe espremedor (Tonk). Polipropileno."),
        ("Balde DUE 30L com Espremedor", "Balde 30L com divisão interna fixa e graduação. Design moderno e resistente, com espremedor de cabo de alumínio."),
        ("Espremedor Tonk", "Espremedor profundo e eficiente, com excelente performance de secagem. Ajuste perfeito no balde 15L. Ideal para refil mop úmido 150-220g."),
        ("Kit Carro Funcional", "Kit com 4 baldes (3L vermelho e verde, 6L azul e amarelo) para limpeza por área, evitando contaminação cruzada. Inclui placa sinalizadora."),
        ("Cabo Extensor 1,40m", "Cabo extensor fixo de 1,40m para mops e acessórios de limpeza. Polipropileno e alumínio."),
        ("Cabo Telescópico 1,80m a 9m", "Cabos telescópicos profissionais que se estendem de 1,8m a 9m, para áreas altas e de difícil acesso."),
        ("Caixa Dobrável", "Caixa dobrável com montagem fácil e sistema de travamento no fundo. Suporta 50kg. Polipropileno."),
        ("Lixeira 12L Click", "Lixeira minimalista com tampa e suporte para bobinas de saco de lixo. ABS e PP."),
        ("Lixeira 12L Push", "Lixeira minimalista sem tampa, com suporte para saco de lixo. ABS e PP."),
        ("Lixeira Porta Saco 15L", "Lixeira porta saco de design minimalista, em 3 modelos: sem aro, com aro e aro + tampa. ABS e PP."),
        ("Lixeira TVV 60L", "Lixeira 60 litros com tampa basculante de ampla abertura. Durabilidade e estabilidade. PP."),
        ("Lixeira Basculante com Pedal 18L", "Lixeira com pedal de alta resistência e abertura de 75°. Encaixe lateral da tampa. 18 litros."),
        ("Lixeira Basculante com Pedal 36L", "Lixeira com pedal de alta resistência e abertura de 75°. 36 litros."),
        ("Lixeira Basculante com Pedal 50L", "Lixeira com pedal de alta resistência e abertura de 75°. 50 litros."),
        ("Lixeira 100L", "Lixeira 100 litros com opção de rodas, alça para deslocamento e abertura de 85°."),
        ("Contentor 120L", "Contentor para lixo 120 litros com rodas, para coleta urbana, lixo hospitalar e resíduos industriais. Abertura de 270°."),
        ("Lixeira 240L", "Lixeira 240 litros com duas rodas de borracha 200mm, para coleta urbana, lixo hospitalar e resíduos industriais."),
        ("Rodo de Borracha 35cm", "Rodo com borracha dupla expandida de alta absorção e durabilidade. Cabo com rosca euro. 35cm."),
        ("Rodo de Borracha 45cm", "Rodo com borracha dupla expandida. Cabo com rosca euro. 45cm."),
        ("Rodo de Borracha 55cm", "Rodo com borracha dupla expandida. 55cm para áreas maiores."),
        ("Rodo de Borracha 65cm", "Rodo com borracha dupla expandida. 65cm para áreas grandes."),
        ("Suporte para Mop Pó", "Suporte para mop pó com 2 hastes metálicas de alta flexibilidade. Ideal com cabo de 140cm. Aço e PP."),
        ("Suporte para Mop Úmido", "Suporte para mop úmido com haste super resistente em formato de presilha, fixa no cabo por rosca euro."),
        ("Suporte Fibra com Alça", "Suporte de fibra manual pensado na segurança em chapas quentes e locais de difícil acesso. Pega mão anatômico."),
        ("Refil Mop Pó", "Refil de mop pó de material de qualidade para limpeza diária de pisos."),
        ("Refil Mop Úmido 330g", "Refil de mop úmido de alta absorção (330g) para limpeza de pisos. Uso profissional."),
        ("Refil Mopinho 170g", "Refil de mop úmido compacto (170g) para áreas menores e limpeza rápida."),
        ("Kit Limpa Tudo", "Kit para limpeza geral: suporte fiber lock azul, fibra verde multiuso, fibra branca e cabo extensor 1,40m."),
        ("Kit Mopinho", "Kit com 3 itens: balde 15L sinalizador, refil mopinho 170g e espremedor. Cores personalizáveis."),
        ("Kit Mop Úmido Completo", "Kit completo: suporte mop úmido, refil mop úmido ponta dobrada e cabo extensor 1,40m."),
        ("Kit Carro Funcional Titan", "Kit mais completo Tonk: carro funcional titan com tampa, balde espremedor due, placa sinalizadora, suporte mop úmido, suporte mop pó 60cm, 2 cabos extensores, refil mop úmido 330g, refil mop pó 60cm e pá coletora."),
        ("Kit Balde Due", "Kit balde due: balde due, placa sinalizadora, suporte mop úmido, cabo extensor preto e refil mop úmido cru."),
     ]),
]

class Command(BaseCommand):
    help = "Popula o catálogo HES com todos os tópicos e produtos do PDF."

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
            # Subcategoria padrão "Geral" (o Produto exige uma subcategoria)
            sub, _ = Subcategoria.objects.get_or_create(
                nome="Geral",
                categoria=categoria,
                defaults={"ativo": True, "ordem": 0},
            )
            for produto_nome, produto_desc in produtos:
                # Busca por NOME + SUBCATEGORIA: permite o mesmo produto
                # aparecer em mais de um tópico do catálogo.
                Produto.objects.get_or_create(
                    nome=produto_nome,
                    subcategoria=sub,
                    defaults={
                        "descricao": produto_desc,
                        "codigo": "",
                        "ativo": True,
                        "destaque": False,
                    },
                )
                total += 1
            resumo.append((cat_nome, len(produtos)))

        self.stdout.write(self.style.SUCCESS(
            f"Seed concluído: {len(CATALOGO)} categorias e {total} produtos."
        ))
        for nome, qtd in resumo:
            self.stdout.write(f"  - {nome}: {qtd} produtos")