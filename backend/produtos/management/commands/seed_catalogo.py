# -*- coding: utf-8 -*-
"""
Seed do catálogo HES Hygiene Solutions.
Cria Categorias (tópicos do catálogo) + Subcategoria "Geral" + todos os produtos,
com a descrição/área de uso de cada um. Pode rodar quantas vezes quiser (get_or_create).
Uso: python manage.py seed_catalogo
"""
from django.core.management.base import BaseCommand
from produtos.models import Categoria, Subcategoria, Produto

class Command(BaseCommand):
    help = "Popula o catálogo com todas as categorias e produtos do PDF."

    def handle(self, *args, **options):
        criados = 0

        # Estrutura: (nome_da_categoria, descricao_da_categoria, [ (nome_produto, descricao_produto), ... ])
        CATALOGO = [
            # ================= LINHA GOLD =================
            ("Linha Gold",
             "Linha premium de dispensers com design sofisticado, alta durabilidade, higiene e elegância para ambientes profissionais e corporativos.",
             [
                ("Dispenser Sabonete Espuma DSE05", "Dispenser de sabonete em espuma da Linha Gold. Ideal para banheiros de empresas, escritórios, shoppings e ambientes corporativos."),
                ("Dispenser Sabonete Líquido DSE10", "Dispenser de sabonete líquido da Linha Gold. Indicado para banheiros institucionais e corporativos."),
                ("Dispenser Papel Toalha Bobina DPB6300", "Dispenser de papel toalha bobina. Uso em sanitários de alto fluxo: empresas, shoppings, escolas e hospitais."),
                ("Dispenser Papel Toalha Interfolhado DPI2400", "Dispenser de papel toalha interfolhado. Ideal para banheiros de empresas, clínicas e ambientes corporativos."),
                ("Dispenser Papel Toalha Interfolhado Mini DPIM1400", "Dispenser de papel toalha interfolhado mini, compacto. Para sanitários de baixo fluxo ou espaços reduzidos."),
                ("Dispenser Coletor de Absorvente DCA1000", "Coletor de absorventes descartáveis. Indicado para banheiros femininos de empresas, shoppings e escolas."),
                ("Dispenser Assento Sanitário DCS1000", "Dispenser de assento sanitário descartável. Higiene extra em banheiros públicos e institucionais."),
                ("Dispenser Guardanapeira Interfolhada DG8000", "Guardanapeira para papel guardanapo interfolhado. Uso em cozinhas, copas, refeitórios e praças de alimentação."),
                ("Dispenser Papel Higiênico DHI8000", "Dispenser de papel higiênico interfolhado. Para banheiros institucionais e de alto tráfego."),
                ("Dispenser Papel Higiênico DPHB8200", "Dispenser de papel higiênico bobina 8 polegadas. Indicado para sanitários de empresas, escolas e hospitais."),
                ("Dispenser Papel Higiênico DPHB1620", "Dispenser de papel higiênico bobina 16 polegadas (duplo). Para banheiros de alto fluxo e uso institucional."),
             ]),

            # ================= LINHA CARE =================
            ("Linha Care",
             "Linha Care de dispensers com design suave e funcional, oferecendo segurança, higiene e praticidade ideais para hospitais, clínicas e ambientes institucionais.",
             [
                ("Dispenser Papel Toalha Bobina DPH-101", "Dispenser de papel toalha bobina da Linha Care. Ideal para hospitais, clínicas e ambientes institucionais."),
                ("Dispenser Papel Toalha Interfolhado DPH-102", "Dispenser de papel toalha interfolhado da Linha Care. Para hospitais, clínicas e instituições de saúde."),
                ("Dispenser Papel Toalha Interfolhado Mini DPH-103", "Dispenser de papel toalha interfolhado mini. Compacto, para clínicas, consultórios e áreas de saúde."),
                ("Dispenser Papel Higiênico DPH-104", "Dispenser de papel higiênico da Linha Care. Indicado para sanitários de hospitais, clínicas e instituições."),
                ("Dispenser Papel Higiênico DPH-105", "Dispenser de papel higiênico da Linha Care, modelo com capacidade extra. Para alto fluxo em ambientes de saúde."),
                ("Dispenser Papel Higiênico DPH-106", "Dispenser de papel higiênico da Linha Care. Uso em banheiros de hospitais e clínicas."),
                ("Dispenser Sabonete Espuma DPH-107", "Dispenser de sabonete em espuma da Linha Care. Higiene segura para hospitais, clínicas e laboratórios."),
                ("Dispenser Sabonete Líquido DPH-108", "Dispenser de sabonete líquido da Linha Care. Para banheiros de hospitais, clínicas e ambientes de saúde."),
                ("Dispenser Coletor de Absorvente DPH-109", "Coletor de absorventes descartáveis da Linha Care. Para banheiros de hospitais, clínicas e empresas."),
                ("Dispenser Assento Sanitário DPH-110", "Dispenser de assento sanitário descartável da Linha Care. Higiene em sanitários de hospitais e clínicas."),
                ("Dispenser Guardanapeira Interfolhada DPH-111", "Guardanapeira interfolhada da Linha Care. Para refeitórios e copas de hospitais e instituições."),
             ]),

            # ================= LINHA STANDARD =================
            ("Linha Standard",
             "Linha Standard de dispensers: funcionalidade, durabilidade e praticidade em design versátil, proporcionando higiene, segurança e economia.",
             [
                ("Dispenser Papel Toalha Bobina ELT-2101", "Dispenser de papel toalha bobina da Linha Standard. Para banheiros de empresas, comércios e escolas."),
                ("Dispenser Papel Toalha Interfolhado ELT-2102", "Dispenser de papel toalha interfolhado. Indicado para sanitários comerciais e institucionais."),
                ("Dispenser Papel Toalha Interfolhado Mini ELT-2103", "Dispenser de papel toalha interfolhado mini. Compacto para comércios e espaços reduzidos."),
                ("Dispenser Papel Higiênico ELT-2104", "Dispenser de papel higiênico da Linha Standard. Para banheiros comerciais e institucionais."),
                ("Dispenser Sabonete Líquido ELT-2105", "Dispenser de sabonete líquido versátil. Para banheiros de empresas, comércio e estabelecimentos em geral."),
                ("Dispenser Sabonete Espuma ELT-2106", "Dispenser de sabonete em espuma. Higiene econômica para banheiros institucionais e comerciais."),
                ("Dispenser Coletor de Absorvente ELT-2107", "Coletor de absorventes descartáveis. Para banheiros femininos de empresas e comércios."),
                ("Dispenser Assento Sanitário ELT-2108", "Dispenser de assento sanitário descartável. Uso em banheiros públicos e comerciais."),
                ("Dispenser Guardanapeira Interfolhada ELT-2109", "Guardanapeira para uso em copas, cozinhas e refeitórios comerciais."),
             ]),

            # ================= EQUIPAMENTOS PROFISSIONAIS =================
            ("Equipamentos Profissionais",
             "Equipamentos desenvolvidos para alto desempenho, segurança e eficiência em ambientes industriais, comerciais e de serviços.",
             [
                ("Diluidor de Produtos Químicos (Sistema Venturi)", "Sistema de diluição de produtos concentrados por Venturi, com diluições precisas por meio do TIP. Fornecimento e instalação. Uso em cozinhas industriais, hospitais e indústrias."),
                ("Dosador para Máquinas de Lavar Louça", "Dosador individual para higienização em máquinas de lavar louça. Indicado para cozinhas de restaurantes, hotéis e indústrias."),
                ("Dosador para Lavanderia", "Dosador individual para processos de lavanderia profissional. Uso em lavanderias hospitalares, industriais e de hotelaria."),
                ("Treinamento de Utilização e Segurança", "Treinamento completo para uso correto e seguro de produtos e equipamentos de limpeza profissional."),
             ]),

            # ================= PAPÉIS INSTITUCIONAIS =================
            ("Papéis Institucionais",
             "Linha de papéis institucionais com alta absorção, resistência e suavidade, garantindo durabilidade, higiene e conforto em cada uso.",
             [
                ("Toalha Papel Bobina 200M PTB8200", "Papel toalha bobina 200m (6x200m). Alta absorção e resistência para sanitários de alto fluxo."),
                ("Toalha Papel Bobina 150M PTB8150", "Papel toalha bobina 150m (6x150m). Para sanitários institucionais e comerciais."),
                ("Papel Higiênico Bobina Folha Dupla PHBD8300", "Papel higiênico bobina folha dupla, 10cm x 300m (8 rolos/caixa). Maciez e resistência para banheiros."),
                ("Papel Higiênico Bobina Folha Simples PHB8300", "Papel higiênico bobina folha simples, 10cm x 300m. Econômico para uso institucional."),
                ("Papel Higiênico Interfolhado Folha Dupla IHI12", "Papel higiênico interfolhado folha dupla, 20x21cm, pacote com 1000 folhas. Para dispensers interfolhados."),
                ("Papel Higiênico Interfolhado Folha Dupla PHCLFD20X10/8000", "Papel higiênico interfolhado folha dupla, 20x10cm, 8.000 folhas/caixa. Para dispensers e alto fluxo."),
                ("Toalha Interfolhada 2 Dobras PTI1250", "Papel toalha interfolhado 2 dobras, 10x21cm, 8.000 folhas/caixa. Higiene sem contato em sanitários."),
                ("Toalha Interfolhada 3 Dobras PTI12400", "Papel toalha interfolhado 3 dobras, 22x23cm, 2.400/12.000 folhas. Para dispensers interfolhados profissionais."),
             ]),

            # ================= HIGIENE PESSOAL =================
            ("Higiene Pessoal",
             "Linha completa de sabonetes líquidos, espuma, antissépticos e álcool em gel para higienização das mãos em escolas, hotéis, hospitais e indústrias.",
             [
                ("PLURON CLOREXIDINE", "Sabonete/antisséptico de mãos à base de clorexidina. Limpeza e higienização das mãos e corpo em segmentos em geral, com glicerina que evita o ressecamento da pele."),
                ("PLURON HANDMAX ERVA DOCE", "Sabonete perfumado para aplicação por espuma e/ou spray. Indicado para limpeza das mãos em empresas, hotéis, clínicas e indústrias."),
                ("PLURON HANDMAX BLUE", "Sabonete líquido perfume floral. Fórmula concentrada que proporciona lavagem eficiente com pequena quantidade. Uso em banheiros institucionais."),
                ("PLURON HANDFOAM", "Sabonete perfumado de aplicação por espuma. Versões Cereja e Avelã, Pêssego e Erva Doce. Higiene eficiente com pequena quantidade."),
                ("PLURON 144 A SEPT", "Sabonete com triclosan na formulação, promovendo proteção e inibição de microrganismos na pele. Para limpeza e assepsia das mãos."),
                ("PLURON 7060 M", "Sabonete para limpeza de graxas e óleos das mãos. Indicado para oficinas mecânicas e indústrias. Aplicação pura, esfregar e enxaguar."),
                ("PLURON FOAM HAND SEPT", "Sabonete espuma antisséptico para limpeza e assepsia das mãos. Formulação específica para dispensers de espuma, ideal para indústrias alimentícias."),
                ("PLURON 147 AG", "Álcool gel 70% antisséptico das mãos. Pronto uso, com emoliente que evita o ressecamento. Testado contra S. choleraesuis, E. coli, S. aureus e P. aeruginosa."),
                ("PLURON 147 BG SEPT", "Álcool 70% com clorexidina para assepsia das mãos. Pode ser aplicado em saboneteiras spray. Testado contra S. choleraesuis, E. coli, S. aureus e P. aeruginosa."),
                ("PLURON ÁLCOOL FOAM", "Álcool antisséptico em espuma, sem necessidade de enxágue. Indicado para antissepsia das mãos com emoliente que evita o ressecamento."),
             ]),

            # ================= TRATAMENTO DE PISO =================
            ("Tratamento de Piso",
             "Produtos para limpeza, remoção de ceras, selamento e brilho de pisos laváveis: mármore, cerâmica, porcelanato, Paviflex, granilite e outros.",
             [
                ("PLURON 7215", "Limpeza de pisos de mármore, borracha, cerâmica e plásticos através de lavadoras automáticas."),
                ("PLURON 7225", "Remoção de ceras de pisos porosos (exceto madeira), sujidades de terra em pisos frios encardidos e gorduras de superfícies, pisos e paredes."),
                ("PLURON 7230", "Limpeza de pisos, paredes, equipamentos e caixas plásticas em indústrias em geral. Fórmula concentrada que penetra rapidamente nas sujidades."),
                ("PLURON TOP REMOVE", "Remoção de ceras e sujidades em Paviflex, Plurigoma, Ardósia, Pedras Naturais, Granilite, Mármore, entre outros (exceto madeira)."),
                ("PLURON SELAFIX", "Base seladora antiderrapante para área interna. Resistência ao tráfego e excelente resistência em diversos tipos de pisos."),
                ("PLURON SELAFIX EX", "Base seladora para área interna e externa. Não inflamável, resistente ao tráfego, promove restauração de pisos laváveis com equipamentos HS e UHS."),
                ("PLURON MAXBRILHO AT", "Cera auto brilho e impermeabilizante para pisos laváveis. Dispensa o uso de enceradeira, é antiderrapante e resistente ao tráfego."),
                ("PLURON TOP BRILHO", "Cera auto brilho 3x1: sela, dá brilho e protege. Polímeros de alta tecnologia com efeito antiderrapante e resistência ao alto tráfego."),
                ("PLURON 7914", "Cera auto brilho para pisos laváveis. Auto brilhante, dispensa enceradeira, é antiderrapante e resistente ao tráfego."),
             ]),

            # ================= LIMPADORES PERFUMADOS E ODORIZANTES =================
            ("Limpadores Perfumados e Odorizantes",
             "Limpadores de uso geral, perfumados e odorizantes para pisos, vidros, superfícies e ambientes.",
             [
                ("PLURON TRIOXY", "Produto concentrado à base de peróxido de hidrogênio e tensoativos. Limpeza geral e alvejamento de superfícies, inclusive sujidades de mofo."),
                ("PLURON 7470", "Limpeza diária de vidros, espelhos, acrílicos, azulejos, fórmica, telefones e superfícies de plásticos, metais e courvin."),
                ("PLURON LIMPADOR CAPIM LIMÃO", "Limpeza manual de pisos laváveis e superfícies de residências, hospitais, condomínios, shoppings, escolas e comércios. Deixa perfume agradável."),
                ("PLURON LIMPADOR PITANGA", "Limpeza manual de pisos laváveis e superfícies, indicado para ambientes institucionais e comerciais, com perfume agradável."),
                ("PLURON MULTI CITRONELA", "Limpeza multiuso com citronela, afastando insetos como moscas, mosquitos e pernilongos."),
                ("PLURON MULTI PORCELANATO", "Produto de baixa espumação para limpeza de pisos de porcelanato e outros tipos de piso."),
                ("PLURON H8 PREMIUM", "Elimina o cheiro de tabaco e atua como odorizante de ambiente. Aplicável em clínicas, estabelecimentos comerciais e afins."),
                ("PLURON H3 HERBAL", "Limpeza de pisos de mármore, borracha, cerâmica e plástica através de mop ou lavadoras automáticas."),
                ("PLURON H2 PREMIUM", "Limpador de vasos sanitários que remove manchas de sais (cálcio, magnésio e ferro), evita manchas e não possui ácido fluorídrico. Seguro para louças sanitárias."),
                ("PLURON H4 MARINE", "Limpeza manual de pisos e superfícies impregnadas com gorduras ou sujidades de natureza arenosa."),
                ("PLURON H5 PREMIUM", "Detergente perfumado para limpeza pesada de pisos e superfícies impregnadas com gorduras."),
                ("PLURON H4 PREMIUM", "Limpeza manual de pisos e superfícies impregnadas com gorduras ou sujidades arenosas. Uso em hospitais, condomínios, shoppings, escolas e hotéis."),
                ("POLLYCLEAN 10.000", "Detergente flotador para limpeza de equipamentos de cozinhas, pias, fogão, fórmicas, plásticos, banheiros, pisos, azulejos, balcões, cerâmica e mármore."),
             ]),

            # ================= DESINFETANTES PERFUMADOS =================
            ("Desinfetantes Perfumados",
             "Desinfetantes com ação bactericida e perfume agradável para pisos e superfícies em geral.",
             [
                ("PLURON SANIT EUCALIPTO", "Desinfetante perfumado eucalipto com ativos bactericida contra Staphylococcus aureus e Salmonella choleraesuis, deixando o ambiente perfumado."),
                ("PLURON SANIT FLORAL", "Desinfetante com ativos bactericida contra S. aureus e S. choleraesuis. Indicado para pisos e superfícies em geral."),
                ("PLURON SANIT FLORAL FRESH", "Desinfetante com ativos bactericida contra Staphylococcus aureus e Salmonella choleraesuis, com perfume floral fresh."),
                ("PLURON SANIT INTENSE FLORAL", "Desinfetante com ativo bactericida contra Staphylococcus aureus e Salmonella choleraesuis, fragrância floral intensa."),
                ("PLURON SANIT INTENSE SUMMER", "Desinfetante perfumado com fragrância intensa. Desinfecção de pisos e superfícies em geral."),
                ("PLURON SANIT INTENSE MARINE", "Desinfetante perfumado com fragrância marine intensa. Para limpeza e desinfecção de pisos e superfícies."),
                ("PLURON SANIT LAVANDA", "Desinfetante perfumado lavanda com ativos bactericida contra S. aureus e S. choleraesuis. Deixa o ambiente perfumado."),
                ("PLURON SANIT MARINE", "Desinfetante perfumado marine com ação bactericida. Para pisos e superfícies em geral."),
                ("PLURON SANIT TOP FLORAL", "Desinfetante com ação bactericida que desinfeta, limpa e odoriza o ambiente. Uso em pisos e superfícies."),
                ("PLURON SANIT TOP LAVANDA", "Desinfetante à base de quaternário de amônio, eficaz contra Coronavírus (SARS-CoV-2/COVID19, MERS e outros). Desinfeta, limpa e odoriza."),
             ]),

            # ================= DESINCRUSTANTES E LIMPA ALUMÍNIO =================
            ("Desincrustantes e Limpa Alumínio",
             "Produtos para desincrustação de gorduras carbonizadas e limpeza de utensílios de alumínio.",
             [
                ("PLURON 7160", "Lava e desengordura pisos, fogões, exaustores, pias, azulejos, geladeiras e banheiros. Fórmula concentrada que penetra rapidamente nas sujidades."),
                ("PLURON 7710 AE", "Limpeza por espuma de equipamentos, pisos e superfícies impregnadas com gorduras carbonizadas e resíduos oleosos em indústrias alimentícias."),
                ("PLURON LA 21", "Detergente de característica ácida para limpeza e brilho de utensílios de alumínio."),
                ("PLURON 7756", "Higienização de pratos, talheres, bandejas, copos, xícaras e utensílios em máquinas de lavar de cozinhas de hotéis, motéis, hospitais, shoppings e escolas."),
                ("PLURON VERSAT", "Limpeza de depósitos de gorduras carbonizadas em utensílios de alumínio (panelas, coifas, frigideiras, assadeiras, latões, tanques, fogões industriais, filtros de coifas e chapas). Também em banho de guarda de formas de queijo."),
             ]),

            # ================= COZINHA INDUSTRIAL E RESTAURANTES =================
            ("Cozinha Industrial e Restaurantes",
             "Linha especialmente formulada para demandas rigorosas de cozinhas industriais, bares, restaurantes, padarias e açougues.",
             [
                ("PLURON TOP GRILL", "Limpeza de fornos, grelhas, chapas, frigideiras e superfícies com gordura carbonizada. Tensoativo espumante que adere à superfície, aumentando a eficiência da limpeza."),
                ("PLURON 236 A", "Limpeza e desincrustação de formas, latões, caixas plásticas, garrafas, louças, ordenhadeiras mecânicas e recipientes. Também para legumes, frutas e verduras."),
                ("PLURON 7888", "Desinfetante para frutas, legumes e verduras. Amplo espectro biocida contra Enterococcus Faecium e Escherichia coli, testado em laboratório credenciado pela ANVISA. Não usar em cobre e alumínio."),
                ("PLURON 7799 A", "Enxágue final de máquinas de lavar louças: promove secagem rápida e elimina manchas. Uso em indústrias alimentícias, hospitais, shoppings, escolas e hotéis."),
                ("PLURON MAQ DUO", "Produto 2x1 para lavagem e secagem de louças em máquinas de lavar louças. Uso em cozinhas industriais, restaurantes e hotéis."),
                ("PLURON MAQ DET", "Detergente para limpeza de pratos, talheres, bandejas, copos e xícaras em máquinas de lavar de cozinhas de hotéis, motéis, hospitais, shoppings, escolas e indústrias alimentícias. Indicado também para caixas plásticas."),
                ("PLURON MAQ SEC", "Enxágue final de máquinas de lavar louças para secagem rápida e eliminação de manchas."),
                ("PLURON MAQ CLOR", "Limpeza de pratos, talheres, bandejas, copos e xícaras em máquinas de lavar. Uso em cozinhas de hotéis, hospitais, escolas e indústrias alimentícias. Não usar em cobre e alumínio."),
                ("PLURON 194 A", "Lava utensílios de cozinha, pisos, paredes, latões, tanques, mesas de trabalho, caminhões-tanque e equipamentos. Elimina sujidades e resíduos de gorduras."),
                ("PLURON 194 AV", "Lava utensílios de cozinha, pisos, paredes, latões, tanques, mesas de trabalho, caminhões-tanque e equipamentos. Elimina sujidades e resíduos de gorduras."),
                ("PLURON 404 A", "Lava utensílios de cozinha, louças, pisos, paredes, latões, tanques e equipamentos em indústrias alimentícias, farmacêuticas e cozinhas industriais. Indicado também para aplicação no óleo de algodão."),
                ("PLURON 406 A", "Limpeza manual de pisos, paredes, latões, tanques, equipamentos, louças e utensílios em indústrias alimentícias e em geral, hospitais e cozinhas industriais."),
                ("PLURON DETERGENTE NEUTRO", "Lava utensílios de cozinha, pisos, paredes, latões, tanques e equipamentos. Reduz a tensão superficial, facilitando a remoção da gordura."),
             ]),

            # ================= LATICÍNIOS =================
            ("Laticínios",
             "Produtos específicos para limpeza e desinfecção de toda a cadeia do leite: ordenha, tanques de transporte, armazenamento e pasteurizadores.",
             [
                ("PLURON ALCALI CLOR", "Produto de baixa espuma para limpeza de ordenhadeiras mecânicas, tanques de recepção, estocagem, misturadores, resfriadores, equipamentos e tubulações. Eficiente na remoção de gorduras e sujidades orgânicas."),
                ("PLURON CLORCIP", "Produto de baixa espuma para limpeza CIP de ordenhadeiras mecânicas, pisos, paredes, equipamentos e garrafões em indústrias de águas minerais. Também para circuitos post mix, chopeiras e máquinas de lavar pratos com dosador eletrônico."),
                ("PLURON 426 A", "Uso manual e por circulação. Limpeza de pisos, paredes, latões, tanques de recepção, resfriadores, tanques de estocagem e equipamentos em indústrias em geral."),
                ("PLURON 327 AS", "Limpeza por circulação (CIP) de tanques, equipamentos, tubulações, pasteurizadores, evaporadores, resfriadores, ordenhadeiras mecânicas e lavagem de garrafas de vidro."),
                ("PLURON 327 CIP", "Limpeza por circulação de pasteurizadores, evaporadores, resfriadores, ordenhadeiras mecânicas e tubulação de aço inox em indústrias de alimentos. Também para gordura carbonizada em fornos, grelhas, chapas e fritadeiras."),
                ("PLURON NITRIC", "Produto ácido de baixa espuma para limpeza por circulação de pasteurizadores, evaporadores, ordenhadeiras mecânicas e desincrustação de máquinas de lavar louças. Remove resíduos minerais, pedras de leite e calcificações."),
                ("PLURON 320 A", "Limpeza ácida de tanques de fermentação e maturação de cerveja, tubulações, pasteurizadores e ganchos em indústrias alimentícias. Também para fosfatização de superfícies metálicas."),
                ("PLURON 418 A", "Limpeza por espuma de superfícies impregnadas com gorduras e resíduos de óleos em indústrias alimentícias, de bebidas e demais manipuladores de alimentos."),
                ("PLURON 446 A", "Limpeza de pisos, azulejos de cozinhas e equipamentos em geral. Não causa corrosão em plásticos, alumínio, cobre e metais galvanizados."),
                ("PLURON 489 AT5", "Limpeza manual ou por espuma de equipamentos, pisos, paredes e superfícies impregnadas com gorduras e resíduos oleosos em indústrias alimentícias, cozinhas, restaurantes e hospitais."),
                ("PLURON 428 A4", "Limpeza por espuma de superfícies impregnadas com gorduras e resíduos oleosos em indústrias alimentícias, cozinhas, restaurantes, shoppings, hospitais, escolas, hotéis e motéis."),
                ("PLURON 447 AE", "Limpeza por espuma e manual de superfícies impregnadas com gorduras, proteínas e resíduos de óleos. Também para pisos, paredes, latões, tanques, equipamentos e banheiros."),
                ("PLURON 489 A", "Limpeza manual ou por espuma de equipamentos, pisos, paredes e superfícies impregnadas com gorduras e resíduos oleosos de indústrias alimentícias e em geral."),
                ("PLURON 490 A", "Remoção de sujidades inorgânicas em ambientes exclusivamente industriais. Para equipamentos em indústrias de alimentos, frigoríficos, farmacêuticas e bebidas."),
                ("PLURON 490 AM", "Remoção de sujidades inorgânicas em ambientes exclusivamente industriais. Uso em indústrias de alimentos, frigoríficos, farmacêuticas e bebidas."),
                ("PLURON ACID FOAM", "Detergente ácido para limpeza externa em indústrias alimentícias, farmacêuticas e cosméticos. Remove sujidades orgânicas/inorgânicas, pedra cervejeira e pedra de leite. Indicado para enchedoras e esteiras."),
                ("PLURON 786 B5", "Aditivo para soluções cáusticas na lavagem de garrafas e nos sistemas CIP. Reduz a frequência da limpeza ácida conforme necessidade."),
                ("PLURON CE 800 B", "Aditivo na lavagem de garrafas e máquinas em geral. Também utilizado como antiespumante. Indicado para aditivar soluções ácidas nos sistemas CIP."),
                ("PLURON 950 PACK", "Limpa e lubrifica esteiras e correntes de transporte de embalagens cartonadas."),
                ("PLURON 461 A1", "Desinfecção de equipamentos, ordenhadeiras mecânicas, tanques de estocagem, válvulas, tubulações, pisos e paredes em indústrias de alimentos. Baixa formação de espuma."),
                ("PLURON 463 AP", "Desinfecção de superfícies, tanques de estocagem, válvulas, tubulações, pisos e paredes em indústrias alimentícias e em geral."),
                ("PLURON 444 A", "Desinfecção manual por imersão ou circulação de equipamentos, tanques, válvulas, tubulações, ordenhadeiras, pisos e paredes. Também para cloração de água e hortifrutícolas."),
                ("PLURON HIDROXYSEPT", "Desinfecção de equipamentos, tanques de estocagem, válvulas, tubulações, pisos e paredes em indústrias de alimentos."),
                ("PLURON 464 A", "Desinfecção de instalações, equipamentos, superfícies, pisos e utensílios em indústrias alimentícias, escolas, creches, hotéis, restaurantes e cozinhas. Elimina odores e age contra bactérias, bolores e leveduras."),
             ]),

            # ================= FRIGORÍFICOS E ABATEDOUROS =================
            ("Frigoríficos e Abatedouros",
             "Linha desenvolvida para atender às normas de higiene dos Ministérios da Saúde e da Agricultura em frigoríficos e abatedouros.",
             [
                ("PLURON 199 A1", "Utilizado por imersão para proteção de ganchos e carretilhas de ferro e aço contra oxidação. Indicado também para fosfatização de superfícies metálicas."),
                ("PLURON 199 A2", "Limpeza e proteção por imersão de ganchos e carretilhas de ferro ou aço contra oxidação."),
                ("PLURON 488 A", "Limpeza por imersão de cozinhadores contínuos ou estáticos, ganchos e carretilhas. Reduz a tensão superficial, facilitando a remoção de gorduras carbonizadas e incrustações."),
                ("PLURON 484 A", "Limpeza manual de pisos, paredes, latões, tanques, equipamentos e caminhões-tanque em indústrias alimentícias, farmacêuticas e em geral."),
                ("PLURON 485 A", "Lava utensílios de cozinha, pisos, paredes, latões, tanques, equipamentos, botas e luvas. Uso em indústrias alimentícias, farmacêuticas e em geral."),
                ("PLURON 485 A SE", "Lava utensílios, pisos, latões, tanques, equipamentos e utensílios em indústrias farmacêuticas e em geral."),
                ("PLURON 485 AE", "Limpeza de pisos, paredes, caminhões-tanque, equipamentos, luvas e botas em indústrias alimentícias, farmacêuticas, hospitais, condomínios, shoppings, escolas, hotéis e clínicas."),
                ("PLURON CLOROFOAM AL", "Limpeza por espuma de superfícies impregnadas com gorduras e resíduos oleosos em indústrias em geral. Possui cloro que auxilia na limpeza e sanitização."),
                ("PLURON DETACLOR", "Limpeza manual ou por espuma de equipamentos, pisos, paredes e superfícies com gorduras e resíduos oleosos. Possui cloro que auxilia na limpeza e sanitização."),
             ]),

            # ================= SUPERMERCADOS =================
            ("Supermercados",
             "Produtos para limpeza e desinfecção de supermercados, padarias, açougues e áreas de manipulação de alimentos.",
             [
                ("PLURON DET CLEAN", "Lava utensílios em geral, pisos, paredes, latões, tanques, mesas de trabalho, equipamentos, luvas e botas. Para limpeza pesada de supermercados e indústrias."),
                ("PLURON TOP GRILL", "Limpeza de fornos, grelhas, chapas, frigideiras e superfícies com gordura carbonizada em padarias, açougues e restaurantes."),
                ("PLURON 7160", "Lava e desengordura pisos, fogões, exaustores, pias, azulejos e banheiros em supermercados e comércios. Fórmula concentrada."),
             ]),

            # ================= LAVANDERIA =================
            ("Lavanderia",
             "Produtos líquidos ou em pó para limpeza e desinfecção de roupas em lavanderias profissionais, hospitalares, industriais e de hotelaria.",
             [
                ("PLURON SOFT PREMIUM", "Amaciante com tecnologia em cápsulas: mantém os tecidos perfumados e macios por muito mais tempo."),
                ("PLURON SOFT INTENSE", "Amaciante perfumado para todos os tipos de tecidos em lavanderias hospitalares, comerciais, industriais e de hotelaria."),
                ("PLURON 909 LC", "Amaciante com toque suave no perfume, para todos os tipos de tecidos em lavanderias profissionais."),
                ("PLURON 835 LL", "Produto 2 em 1: amacia e acidula roupas de todos os tipos de tecidos em lavanderias hospitalares, comerciais, industriais e de hotelaria."),
                ("PLURON PASSE PRONTO", "Produto para todos os tipos de roupas, oferecendo maior rapidez e qualidade na hora de passar e deixando perfume agradável."),
                ("PLURON 836 LL", "Alveja e desinfeta roupas brancas e de cores firmes de algodão e algodão/poliéster. Não causa manchas em presença de clorexidina."),
                ("PLURON 920 LL4", "Assepsia, remoção de manchas e alvejamento de roupas de algodão/poliéster brancas ou coloridas. Não causa manchas em presença de clorexidina."),
                ("PLURON 960 L", "Alvejante em pó que remove manchas de sangue, frutas, molhos, bebidas e remédios. Para roupas brancas e coloridas. Promove assepsia e não revela manchas de clorexidina."),
                ("PLURON MAXCLOR", "Alveja e desinfeta roupas de algodão e algodão/poliéster. Ampla ação biocida contra S. aureus, Salmonella choleraesuis e Pseudomonas aeruginosa. Elimina traças."),
                ("PLURON 985 L", "Acidulante e anticloro nos processos de lavagem de roupas brancas ou coloridas. Aumenta a vida útil das peças e diminui irritações na pele."),
                ("PLURON 834 LL", "Para sistemas de lavagem de roupas industriais e hospitalares, manual ou com bomba. Possui branqueador óptico que deixa as roupas mais brancas."),
                ("PLURON 888 LLO", "Remoção de gorduras, sangue e medicamentos em roupas de algodão e poliéster/algodão. Possui branqueador óptico que realça o brilho."),
                ("PLURON MAX DETERGENTE EM PÓ", "Detergente para lavagem de roupas de cama, banho e uso pessoal. Eficiente na remoção de sujidades de roupas hospitalares, de hotéis e lavanderias profissionais."),
                ("PLURON CIP LAVANDERIA", "Aditivo alcalino em processos de lavagem de roupas brancas ou coloridas com sujidade média ou pesada. Não agride cores e fibras."),
                ("PLURON 961 L", "Umectação e lavagem de roupas. Pode ser utilizado com um detergente alcalino."),
                ("PLURON 962 L", "Umectação e lavagem de roupas. Apropriado para tecidos delicados como seda, lã, nylon e cobertores. Não agride cores e fibras."),
                ("PLURON 949 L", "Acidulante e anticloro nos processos de lavagem de roupas brancas ou coloridas."),
                ("PLURON INIBY LAV", "Neutraliza resíduos revelados em processos de lavagem por detergentes clorados (clorexidina) e remove manchas de protetores solares, bronzeadores e lubrificantes."),
                ("PLURON CLOTH WASH WHITE", "Lava roupas líquido sem perfume e sem corante, para roupas de cama, banho e uso pessoal. Indicado para roupas brancas e coloridas, com alto teor de branqueador óptico."),
                ("PLURON CLOTH WASH", "Lava roupas líquido perfumado para roupas de cama, banho e uso pessoal. Todos os tipos de tecido."),
                ("PLURON LAVA ROUPAS", "Detergente para todos os tipos de roupas. Possui alcanolamida de ácidos graxos de coco que evita o ressecamento da pele. Não agride fibras e cores."),
                ("PLURON DETACID L", "Tratamento de roupas manchadas de gorduras, óleos, graxas e batom/maquiagem. Não enfraquece fibras nem destrói tecidos de algodão e algodão/poliéster."),
                ("PLURON LAV SOLV", "Remoção de manchas de gorduras, óleos, molhos e batom. Tensoativo de baixa formação de espuma."),
                ("PLURON LAV CLEAN", "Lava roupas líquido sem perfume e sem corante, para roupas de cama, banho e uso pessoal, indicado para roupas brancas e coloridas."),
                ("PLURON 833 LL", "Contém sequestrantes e dispersantes que evitam o amarelamento da roupa pela absorção de sais de cálcio e ferro."),
                ("PLURON ALCALAV", "Possui branqueador óptico que deixa as roupas mais brancas e tensoativos biodegradáveis de baixa formação de espuma."),
                ("PLURON 911 LLX", "Usado associado a detergente neutro em processos de lavagem de roupas brancas ou coloridas com sujidade média ou pesada."),
                ("PLURON 837 LL3", "Anticloro e acidulante nos processos de lavagem de roupas brancas ou coloridas. Reduz o número de enxágues, o tempo e o consumo de água. Elimina traças."),
                ("PLURON 847 LLF", "Acidulante e removedor de ferrugem no processo ou uso local de roupas brancas ou coloridas. Não aplicar em superfícies não resistentes a ácidos."),
                ("PLURON 964 L", "Pré-lavagem e lavagem de roupas com sujidade pesada em lavanderias industriais. Pode ser usado em materiais sintéticos como polipropileno."),
             ]),

            # ================= FARMACÊUTICA E HOSPITALAR =================
            ("Farmacêutica e Hospitalar",
             "Linha completa para o setor farmacêutico e hospitalar, em conformidade com as normas do Ministério da Saúde e ANVISA.",
             [
                ("PLURON 147 BG SEPT SAÚDE", "Álcool 70% com clorexidina, pronto uso, antisséptico das mãos. Testado contra S. aureus, Salmonella choleraesuis, P. aeruginosa e E. coli (laudo ANVISA). Com emoliente."),
                ("PLURON ÁLCOOL FOAM SAÚDE", "Álcool antisséptico em espuma, pronto uso, sem enxágue. Testado contra S. choleraesuis, E. coli, S. aureus e P. aeruginosa."),
                ("PLURON 147 AG SAÚDE", "Álcool em gel 70% antisséptico das mãos à base de álcool etílico, com antissepsia imediata. Amplo espectro testado em laboratório credenciado pela ANVISA."),
                ("SAMPROX 3,5%", "Ácido peracético para esterilização de dialisadores, linhas de hemodiálise e desinfecção de alto nível de máquinas de hemodiálise. Produto com proteção UV nas embalagens de 5L. Proibido uso por imersão."),
                ("SAMPROX 5%", "Esterilização de dialisadores e linhas de hemodiálise e desinfecção de alto nível das máquinas de hemodiálise. Laudos ANVISA de eficácia e segurança."),
                ("PLURON QUATER LH", "Desinfetante à base de quaternário de amônio de 5ª geração e biguanida. Para desinfecção de superfícies fixas e artigos não críticos em hospitais e estabelecimentos de saúde. Eficaz contra KPC, C. Albicans, Acinetobacter e Coronavírus."),
             ]),

            # ================= AUTOMOTIVA =================
            ("Automotiva",
             "Linha automotiva: limpeza de chassis, carrocerias, motores e rodas até conservação geral de veículos. Ideal para transportadoras, postos, lava-jatos e empresas de ônibus.",
             [
                ("MUSTANG SILICONE GEL", "Renova e revitaliza superfícies de borracha, vinil e plásticos do veículo. Restaura o brilho original protegendo contra sol e tempo."),
                ("MUSTANG PRIMA", "Renova superfícies emborrachadas como pneus e tapetes de veículos. Aplicação fácil, com aparência de pneus novos."),
                ("SOLUMOL 960 R", "Detergente para embelezamento automotivo. Realça o brilho da pintura na primeira lavagem."),
                ("SUPERMIX CR", "Lavagem manual ou automática de veículos e equipamentos com superfícies pintadas."),
                ("MUSTANG AZULÃO", "Limpeza super pesada para carrocerias de madeira, alumínio, chassis, motores e sujidades intensas. Limpeza profunda que realça o brilho da pintura."),
                ("POLLYCLEAN E", "Limpeza de chassis, motores, rodas, caminhões com carrocerias de madeira, baú e tanques pintados."),
                ("SUPREMIX AT", "Limpeza de pisos, equipamentos de inox e alumínio, pátios de manobra e frotas de veículos em indústrias alimentícias e em geral."),
                ("MUSTANG SOLUMAX DR 8", "Detergente desengraxante concentrado para limpeza impecável. Elimina sujeiras pesadas: graxas, óleos e resíduos betuminosos. Também para chassis, motores, rodas e baús."),
             ]),

            # ================= ACESSÓRIOS DE LIMPEZA =================
            ("Acessórios de Limpeza",
             "Acessórios profissionais para rotinas de limpeza: panos, baldes, lixeiras, rodos, mops, pulverizadores, sinalização e kits.",
             [
                ("Espátula", "Limpador para box, janelas, frestas e fendas. Cabo anatômico, super resistente e fácil de limpar. Acompanha 2 refis de microfibra. Polipropileno."),
                ("Pá Coletora", "Pá coletora com tampa e cabo de alumínio. Trava na tampa mantendo-a aberta para descarte seguro. Polipropileno e microfibra, 600g."),
                ("Limpa Vidros", "Limpador profissional para vidros e superfícies lisas. Cabo anatômico e fácil higienização."),
                ("Pano de Microfibra", "Pano de microfibra de alta absorção. Elimina poeira, sujeira e graxa sem arranhar nem soltar fiapos. Kits com 4, 6 ou 12 unidades (300 a 500mm)."),
                ("Organizador para Cabos", "Organiza equipamentos de limpeza e otimiza o armazenamento, mantendo os cabos presos firmemente. Polipropileno. Kit com 3 a 6 suportes."),
                ("Tela para Mictório", "Tela odorizadora com furos anti respingos, embalada individualmente, mantendo a fragrância por mais tempo. Fragrâncias: fruit-fruit, canela, citrus e algas. PVC injetável."),
                ("Placas Sinalizadoras", "Placas para sinalizar e interditar áreas na prevenção de acidentes: cuidado, piso molhado, não entre, área em manutenção, limpeza em andamento. Leves e resistentes a impactos."),
                ("Pulverizador 500ml", "Pulverizador profissional de uso contínuo com alta resistência química. Design ergonômico com gatilho ajustável. 500ml."),
                ("Pulverizador 1L", "Pulverizador profissional de alta resistência química e durabilidade para rotinas intensas. Gatilho ajustável. 1 litro."),
                ("Balde 3 Litros", "Balde 3L com graduação interna para diluição correta de produtos. Prático, ergonômico e com bico dosador na borda. Polipropileno + ABS."),
                ("Balde 6 Litros", "Balde 6L com graduação interna e bico dosador. Para limpeza geral e separação de resíduos. Polipropileno + ABS."),
                ("Kit Carro Funcional", "Kit com 4 baldes (3L vermelho e verde, 6L azul e amarelo) para limpeza por área, evitando contaminação cruzada. Inclui placa sinalizadora."),
                ("Balde 15L Reforçado", "Balde 15 litros com alça, ideal para limpeza de pequenas áreas. Acompanha ou recebe espremedor (Tonk). Polipropileno."),
                ("Balde DUE 30L com Espremedor", "Balde 30L com divisão interna fixa e graduação para diluição. Design moderno e resistente, com espremedor de cabo de alumínio. Polipropileno."),
                ("Espremedor Tonk", "Espremedor profundo e eficiente, com excelente performance de secagem. Ajuste perfeito no balde 15L e encaixe para cabo de alumínio. Ideal para refil mop úmido 150-220g."),
                ("Cabo Extensor 1,40m", "Cabo extensor fixo de 1,40m para mops e acessórios de limpeza. Polipropileno e alumínio."),
                ("Cabo Telescópico 1,80m", "Cabo telescópico com capacidade de extensão, montagem fácil e rápida. Polipropileno e alumínio."),
                ("Cabo Telescópico 3m/4,5m/6m/9m", "Cabos telescópicos profissionais que se estendem de 1,8m a 9m, para limpeza de áreas altas e de difícil acesso. Polipropileno e alumínio."),
                ("Caixa Dobrável", "Caixa dobrável com montagem fácil, sistema de travamento no fundo. Suporta 50kg (5 caixas desmontadas = 1 montada). Polipropileno."),
                ("Lixeira 12L Click", "Lixeira minimalista com tampa (modelo Click) e suporte para bobinas de saco de lixo. ABS e PP."),
                ("Lixeira 12L Push", "Lixeira minimalista sem tampa (modelo Push) com sistema inovador de suporte para saco de lixo. ABS e PP."),
                ("Lixeira Porta Saco 15L", "Lixeira porta saco de design minimalista, em 3 modelos: sem aro, com aro e aro + tampa. ABS e PP."),
                ("Lixeira TVV 60L", "Lixeira 60 litros com tampa basculante de ampla abertura, durabilidade e estabilidade para ambientes que exigem higiene e organização. PP."),
                ("Lixeira Basculante com Pedal 18L", "Lixeira com pedal de alta resistência e abertura de 75°. Encaixe lateral da tampa. 18 litros. PP."),
                ("Lixeira Basculante com Pedal 36L", "Lixeira com pedal de alta resistência e abertura de 75°. 36 litros. Material: metal opcional."),
                ("Lixeira Basculante com Pedal 50L", "Lixeira com pedal de alta resistência e abertura de 75°. 50 litros. Metálica ou plástica."),
                ("Lixeira 100L", "Lixeira 100 litros com opção de rodas, alça para deslocamento e abertura de 85°. Rodas silenciosas e discretas. PP."),
                ("Contentor 120L", "Contentor para lixo 120 litros com rodas, para coleta urbana, lixo hospitalar e resíduos industriais. Abertura de 270°. PP e inox."),
                ("Lixeira 240L", "Lixeira 240 litros com duas rodas de borracha 200mm, para coleta urbana, lixo hospitalar e resíduos industriais. Design ergonômico. PP."),
                ("Rodo de Borracha 35cm", "Rodo com borracha dupla expandida de alta absorção e durabilidade. Cabo com rosca euro. 35cm. PP."),
                ("Rodo de Borracha 45cm", "Rodo com borracha dupla expandida de alta absorção. Cabo com rosca euro. 45cm. PP."),
                ("Rodo de Borracha 55cm", "Rodo com borracha dupla expandida. 55cm para áreas maiores. PP."),
                ("Rodo de Borracha 65cm", "Rodo com borracha dupla expandida. 65cm para áreas grandes. PP."),
                ("Suporte para Mop Pó", "Suporte para mop pó com 2 hastes metálicas de alta flexibilidade. Ideal com cabo de 140cm. Aço e PP."),
                ("Suporte para Mop Úmido", "Suporte para mop úmido com haste super resistente em formato de presilha, fixa no cabo por rosca euro. PP."),
                ("Suporte Fibra com Alça", "Suporte de fibra manual pensado na segurança em chapas quentes e locais de difícil acesso. Pega mão anatômico. PP."),
                ("Refil Mop Pó", "Refil de mop pó de material de qualidade para limpeza diária de pisos. Uso com suporte e cabo adequados."),
                ("Refil Mop Úmido 330g", "Refil de mop úmido de alta absorção (330g) para limpeza de pisos. Uso profissional."),
                ("Refil Mopinho 170g", "Refil de mop úmido compacto (170g) para áreas menores e limpeza rápida."),
                ("Kit Limpa Tudo", "Kit para limpeza geral: suporte fiber lock azul, fibra verde multiuso, fibra branca e cabo extensor 1,40m."),
                ("Kit Mopinho", "Kit composto por 3 itens: balde 15L sinalizador, refil mopinho 170g e espremedor. Cores personalizáveis."),
                ("Kit Mop Úmido Completo", "Kit completo: suporte mop úmido, refil mop úmido ponta dobrada e cabo extensor 1,40m."),
                ("Kit Carro Funcional Titan", "Kit mais completo Tonk: carro funcional titan com tampa, balde espremedor due, placa sinalizadora, suporte de mop úmido, suporte de mop pó 60cm, 2 cabos extensores, refil mop úmido 330g, refil mop pó 60cm e pá coletora."),
                ("Kit Balde Due", "Kit balde due: balde due, placa sinalizadora, suporte mop úmido, cabo extensor preto e refil mop úmido cru."),
             ]),
        ]

        total_produtos = 0
        for cat_nome, cat_desc, produtos in CATALOGO:
            categoria, _ = Categoria.objects.get_or_create(
                nome=cat_nome, defaults={"descricao": cat_desc, "ativo": True}
            )
            # Subcategoria padrão "Geral" (o modelo exige subcategoria no produto)
            sub, _ = Subcategoria.objects.get_or_create(
                nome="Geral", categoria=categoria,
                defaults={"ativo": True, "ordem": 0},
            )
            for nome, descricao in produtos:
                _, criado = Produto.objects.get_or_create(
                    nome=nome,
                    defaults={
                        "subcategoria": sub,
                        "codigo": "",
                        "descricao": descricao,
                        "ativo": True,
                        "destaque": False,
                    },
                )
                if criado:
                    criados += 1
                total_produtos += 1

        self.stdout.write(self.style.SUCCESS(
            f"Seed concluído: {len(CATALOGO)} categorias, {total_produtos} produtos no catálogo "
            f"({criados} criados agora, os demais já existiam)."
        ))