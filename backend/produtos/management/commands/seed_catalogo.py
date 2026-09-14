# -*- coding: utf-8 -*-
"""
Seed do catálogo HES Hygiene Solutions — versão definitiva.
17 categorias seguindo as seções do catálogo, com códigos e descrições.

Uso:
    python manage.py seed_catalogo --reset   # apaga e recria (substitui o catálogo antigo)
"""
from django.core.management.base import BaseCommand
from django.db import transaction
from produtos.models import Categoria, Subcategoria, Produto

CATALOGO = [
    # ============ 1. DISPENSERS — LINHA GOLD ============
    ("Dispensers — Linha Gold",
     "Dispensers de alta durabilidade e acabamento elegante para ambientes profissionais e corporativos.",
     [
        ("Dispenser Papel Toalha Bobina", "DPB6300", "Sistema de corte e proteção contra umidade, indicado para alto fluxo."),
        ("Dispenser Papel Toalha Interfolhado", "DPI2400", "Retirada folha a folha, reduz desperdício e protege o papel."),
        ("Dispenser Papel Toalha Interfolhado Mini", "DPIM1400", "Versão compacta para espaços reduzidos."),
        ("Dispenser Papel Higiênico Interfolhado", "DHI8000", "Liberação folha a folha, com proteção contra contaminação."),
        ("Dispenser Papel Higiênico Bobina (DPHB8200)", "DPHB8200", "Para rolos de 8.200 m, reposição prática."),
        ("Dispenser Papel Higiênico Bobina (DPHB1620)", "DPHB1620", "Para rolos de 1.620 m, uso contínuo."),
        ("Dispenser Sabonete Espuma", "DSE05", "Acionamento por bomba com dosagem controlada."),
        ("Dispenser Sabonete Líquido", "DSE10", "Alta capacidade, com válvula dosadora."),
        ("Dispenser Coletor de Absorvente", "DCA1000", "Descarte higiênico e isolado na cabine."),
        ("Dispenser Coletor de Assento Sanitário", "DCS1000", "Dispenser para assepsia do assento."),
        ("Dispenser Guardanapeira Interfolhada", "DG8000", "Libera um guardanapo por vez."),
     ]),

    # ============ 2. DISPENSERS — LINHA CARE ============
    ("Dispensers — Linha Care",
     "Design suave e funcional para hospitais, clínicas e ambientes institucionais.",
     [
        ("Dispenser Papel Toalha Bobina (DPH-101)", "DPH-101", "Corte facilitado e estrutura resistente."),
        ("Dispenser Papel Toalha Bobina (DPH-102)", "DPH-102", "Versão adicional da linha funcional."),
        ("Dispenser Papel Toalha Interfolhado", "DPH-103", "Retirada individual e higiênica."),
        ("Dispenser Papel Higiênico Interfolhado", "DPH-104", "Proteção com retirada folha a folha."),
        ("Dispenser Papel Higiênico Bobina (DPH-105)", "DPH-105", "Tampa de proteção e encaixe seguro."),
        ("Dispenser Papel Higiênico Bobina (DPH-106)", "DPH-106", "Modelo complementar da linha."),
        ("Dispenser Sabonete Espuma", "DPH-107", "Design suave e funcional para hospitais e clínicas."),
        ("Dispenser Sabonete Líquido", "DPH-108", "Acionamento ergonômico para higiene institucional."),
        ("Dispenser Coletor de Absorvente", "DPH-109", "Descarte isolado, contribui para o bom odor do ambiente."),
        ("Dispenser Coletor de Assento Sanitário", "DPH-110", "Higienização do assento antes do uso."),
        ("Dispenser Guardanapeira Interfolhada", "DPH-111", "Liberação de uma folha por vez."),
     ]),

    # ============ 3. DISPENSERS — LINHA STANDART ============
    ("Dispensers — Linha Standart",
     "Funcionalidade, durabilidade e praticidade em design versátil, proporcionando higiene, segurança e economia.",
     [
        ("Dispenser Sabonete Líquido", "ELT-2105", "Funcional, durável e com bom custo-benefício."),
        ("Dispenser Sabonete Espuma", "ELT-2106", "Acionamento simples e manutenção fácil."),
        ("Dispenser Papel Toalha Bobina", "ELT-2101", "Estrutura versátil e resistente."),
        ("Dispenser Papel Toalha Interfolhado", "ELT-2102", "Prático e econômico."),
        ("Dispenser Papel Toalha Interfolhado Mini", "ELT-2103", "Compacto, para espaço reduzido."),
        ("Dispenser Papel Higiênico", "ELT-2104", "Modelo para uso contínuo, com reposição prática."),
        ("Dispenser Coletor de Absorvente", "ELT-2107", "Descarte higiênico em cabines sanitárias."),
        ("Dispenser Coletor de Assento Sanitário", "ELT-2108", "Dispenser para assepsia do assento."),
        ("Dispenser Guardanapeira Interfolhada", "ELT-2109", "Operação simples, uso institucional."),
     ]),

    # ============ 4. EQUIPAMENTOS / SISTEMAS ============
    ("Equipamentos / Sistemas de Limpeza Profissional",
     "Equipamentos para alto desempenho, segurança e eficiência em ambientes industriais, comerciais e de serviços.",
     [
        ("Diluidores", "", "Equipamentos para diluição de produtos químicos concentrados via sistema Venturi, com diluições precisas."),
        ("Dosadores", "", "Dosadores individuais para processos de higienização em máquinas de lavar louça e lavanderias."),
        ("Treinamento", "", "Treinamento para o uso correto e seguro dos produtos e equipamentos fornecidos."),
     ]),

    # ============ 5. PAPÉIS INSTITUCIONAIS ============
    ("Linha de Papéis Institucionais",
     "Alta absorção, resistência e suavidade, com responsabilidade ecológica.",
     [
        ("Toalha Bobina 200m", "PTB8200", "Alta absorção e resistência; caixa com 6 unidades."),
        ("Toalha Bobina 150m", "PTB8150", "Macia e resistente; caixa com 6 unidades."),
        ("Toalha Interfolhada 2 Dobras", "PTI1250", "20 x 21 cm, absorvente e suave; 8.000 folhas/caixa."),
        ("Toalha Interfolhada 3 Dobras", "PTI12400", "22 x 23 cm, maior resistência; 2.400 folhas/caixa."),
        ("Higiênico Bobina Folha Dupla", "PHBD8300", "10 cm x 300 m; macio e resistente."),
        ("Higiênico Bobina Folha Simples", "PHB8300", "10 cm x 300 m; econômico e resistente."),
        ("Higiênico Interfolhado Folha Dupla (IHI12)", "IHI12", "20 x 21 cm, 1.000 folhas; suave e absorvente."),
        ("Higiênico Interfolhado Folha Dupla (PHCLFD20X10/8000)", "PHCLFD20X10/8000", "10 x 21 cm, 8.000 folhas; econômico para alto volume."),
     ]),

    # ============ 6. HIGIENE PESSOAL / MUSTANG PLURON ============
    ("Higiene Pessoal / Institucional — Mustang Pluron",
     "Linha completa de limpeza de alta qualidade para escolas, hotéis, motéis, supermercados e espaços institucionais.",
     [
        ("Pluron Handmax Erva Doce", "", "Sabonete com glicerina e alcanolamida que evita o ressecamento da pele."),
        ("Pluron Clorexidine", "", "Sabonete perfumado para aplicação por espuma e/ou spray, para limpeza das mãos."),
        ("Pluron 7060 M", "", "Sabonete para limpeza de graxas e óleos das mãos em oficinas e indústrias."),
        ("Pluron Foam Hand Sept", "", "Limpeza e assepsia das mãos, específico para dispensers de espuma."),
        ("Pluron Handmax Blue", "", "Limpeza de mãos com perfume floral; fórmula concentrada e econômica."),
        ("Pluron 144 A Sept", "", "Contém triclosan, protege e inibe microrganismos na pele."),
        ("Pluron Handfoam", "", "Sabonete perfumado por espuma; versões Cereja e Avelã, Pêssego e Erva Doce."),
        ("Pluron 147 AG", "", "Álcool gel 70% antisséptico das mãos, sem necessidade de enxágue."),
        ("Pluron Álcool Foam", "", "Antisséptico das mãos por espuma, sem necessidade de enxágue."),
        ("Pluron 147 BG Sept", "", "Álcool 70% com clorexidina para assepsia das mãos."),
        ("Pluron 7215", "", "Limpeza de pisos de mármore, borracha, cerâmica e plástico com lavadoras automáticas."),
        ("Pluron 7225", "", "Remove ceras de pisos porosos (exceto madeira) e sujidades de terras em pisos encardidos."),
        ("Pluron 7250", "", "Limpeza de pisos e superfícies para uso geral."),
        ("Pluron Top Remove", "", "Remove ceras e sujidades em Paviflex, Plurigoma, Ardósia, Pedras Naturais, Granilite e Mármore."),
        ("Pluron Selafix", "", "Base seladora para área interna; antiderrapante e não inflamável."),
        ("Pluron Selafix EX", "", "Base seladora para área interna e externa; resistente ao tráfego."),
        ("Pluron Maxbrilho AT", "", "Cera auto brilho e impermeabilizante para pisos laváveis; dispensa enceradeira."),
        ("Pluron 7914", "", "Cera auto brilhante, antiderrapante e resistente ao tráfego."),
        ("Pluron Top Brilho", "", "Cera 3x1: sela, dá brilho e protege; alta aderência e efeito antiderrapante."),
     ]),

    # ============ 7. LIMPADORES PERFUMADOS / ODORIZANTES ============
    ("Limpadores Perfumados / Odorizantes",
     "Limpadores de uso geral, perfumados e odorizantes para pisos, vidros, superfícies e ambientes.",
     [
        ("Pluron Trioxy", "", "Limpeza à base de peróxido de hidrogênio; ação contra mofo."),
        ("Pluron 7470", "", "Limpeza diária de vidros, espelhos, fórmicas, plásticos, metais e courvin."),
        ("Pluron Limpador Capim Limão", "", "Pisos laváveis e superfícies de residências, hospitais, hotéis, escritórios, etc."),
        ("Pluron Limpador Pitanga", "", "Mesma indicação do Capim Limão; deixa perfume agradável."),
        ("Pluron Multi Citronela", "", "Contém citronela, afasta insetos indesejáveis."),
        ("Pluron Multi Porcelanato", "", "Limpeza de porcelanatos e outros tipos de pisos."),
        ("Pluron H8 Premium", "", "Limpeza de pisos de mármore, borracha, cerâmica e plástica."),
        ("Pluron H3 Herbal", "", "Eliminador de odores de tabaco e de ambiente."),
     ]),

    # ============ 8. DESINFETANTES PERFUMADOS ============
    ("Desinfetantes Perfumados",
     "Desinfetantes com ação bactericida e perfume agradável para pisos e superfícies em geral.",
     [
        ("Pluron Sanit Eucalipto", "", "Ação bactericida contra S. aureus e S. choleraesuis."),
        ("Pluron Sanit Floral", "", "Ação bactericida."),
        ("Pluron Sanit Floral Fresh", "", "Ação bactericida."),
        ("Pluron Sanit Intense Floral", "", "Ação bactericida."),
        ("Pluron Sanit Intense Summer", "", "Ação bactericida."),
        ("Pluron Sanit Intense Marine", "", "Ação bactericida."),
        ("Pluron Sanit Lavanda", "", "Ação bactericida."),
        ("Pluron Sanit Marine", "", "Ação bactericida."),
        ("Pluron Sanit Top Floral", "", "Ação contra Coronavírus (cepa MHV) e SARS-CoV-2."),
        ("Pluron Sanit Top Lavanda", "", "Ação contra Coronavírus (cepa MHV) e SARS-CoV-2."),
     ]),

    # ============ 9. DETERGENTES PERFUMADOS ============
    ("Detergentes Perfumados",
     "Detergentes perfumados para limpeza de equipamentos, superfícies, pisos e ambientes.",
     [
        ("Pollyclean 10.000", "", "Limpeza de equipamentos de cozinhas, pisos, fogão, azulejos, etc."),
        ("Pluron H2 Premium", "", "Limpador de vasos sanitários; remove cálcio, magnésio e ferro."),
        ("Pluron H4 Marine", "", "Limpeza de pisos com gorduras ou sujidades de natureza arenosa."),
        ("Pluron H5 Premium", "", "Limpeza de gorduras pesadas."),
        ("Pluron H4 Premium", "", "Limpeza de pisos e superfícies com gorduras ou sujidade arenosa."),
     ]),

    # ============ 10. LAVA LOUÇAS ============
    ("Cozinha Industrial e Restaurantes — Lava Louças",
     "Linha para higienização de louças em máquinas de lavar de cozinhas industriais, restaurantes e hotéis.",
     [
        ("Pluron 236 A", "", "Limpeza e desincrustação de louças, caixas plásticas, etc."),
        ("Pluron 7756", "", "Higienização de pratos, talheres, bandejas, copos, etc."),
        ("Pluron 7799 A", "", "Enxágue final para máquinas de lavar louças; evita manchas."),
        ("Pluron Maq Duo", "", "Abrilhantador e secagem de louças em máquinas."),
        ("Pluron Maq Det", "", "Limpeza de pratos, talheres, etc., em máquinas."),
        ("Pluron Maq Sec", "", "Enxágue final em máquinas; secagem rápida."),
        ("Pluron Maq Clor", "", "Limpeza de pratos, talheres, etc."),
     ]),

    # ============ 11. DESINCRUSTANTES / LIMPA ALUMÍNIO ============
    ("Desincrustantes / Limpa Alumínio",
     "Produtos para desincrustação de gorduras carbonizadas e limpeza de utensílios de alumínio.",
     [
        ("Pluron 7160", "", "Desincrustante para fornos, grelhas, chapas e fogões."),
        ("Pluron 7710 AE", "", "Limpeza por espuma de equipamentos e superfícies com gorduras carbonizadas."),
        ("Pluron Top Grill", "", "Limpeza de fornos, grelhas, chapas e frigideiras."),
        ("Pluron LA 21", "", "Detergente para limpeza e brilho de utensílios de alumínio."),
     ]),

    # ============ 12. DETERGENTE / SANITIZANTE EM PÓ ============
    ("Detergente / Sanitizante em Pó",
     "Produtos em pó para sanitização e desincrustação.",
     [
        ("Pluron 7688", "", "Desinfetante para frutas, legumes e verduras."),
        ("Pluron Versat", "", "Limpeza de depósitos de gorduras carbonizadas em utensílios de alumínio e aço."),
     ]),

    # ============ 13. DETERGENTE NEUTRO ============
    ("Detergente Neutro",
     "Detergentes neutros para limpeza de utensílios, pisos, paredes e bancadas.",
     [
        ("Pluron 194 A", "", "Limpeza de utensílios de cozinha, pisos, paredes e mesas de trabalho."),
        ("Pluron 194 AV", "", "Mesma aplicação do 194 A."),
        ("Pluron 404 A", "", "Limpeza de utensílios de cozinha, pisos, paredes e mesas de trabalho."),
        ("Pluron 406 A", "", "Limpeza manual de paredes, pisos, bancadas e mesas de trabalho."),
        ("Pluron Detergente Neutro", "", "Limpeza de utensílios de cozinha, pisos, paredes e bancadas."),
     ]),

    # ============ 14. LATICÍNIOS — LIMPEZA GERAL ============
    ("Laticínios — Limpeza Geral",
     "Produtos para limpeza e desinfecção de toda a cadeia do leite: ordenha, tanques, armazenamento e pasteurizadores.",
     [
        ("Pluron Alcali Clor", "", "Detergente de alta espuma para limpeza CIP."),
        ("Pluron Clorcip", "", "Detergente de espuma para limpeza CIP (equipamentos e garrafas)."),
        ("Pluron 236 A Laticínios", "", "Detergente para limpeza manual e circulação (pisos, paredes, mesas, tanques)."),
        ("Pluron 436 A", "", "Detergente para limpeza manual e circulação; remoção de gorduras carbonizadas."),
        ("Pluron 194 A Laticínios", "", "Limpeza de utensílios de cozinha, pisos e paredes."),
        ("Pluron 194 AV Laticínios", "", "Fórmula similar ao 194 A."),
        ("Pluron 327 AS", "", "Limpeza por circulação em tanques, equipamentos e tubulações."),
        ("Pluron 337 AB", "", "Limpeza por circulação em tanques e tubulações de aço inox."),
        ("Pluron 327 CIP", "", "Limpeza por circulação em tanques, evaporadores e tubulações."),
        ("Pluron Nitric", "", "Ácido de baixa espuma para circulação em tanques e concentradores."),
        ("Pluron 320 A", "", "Limpeza de tanques de fermentação e maturação de cerveja."),
        ("Pluron TS 787 B", "", "Limpeza por circulação em trocadores de calor."),
        ("Pluron 950 Pack", "", "Lubrificação de esteiras e correntes de transporte de embalagens."),
        ("Pluron Clorofoam AL", "", "Limpeza por espuma de superfícies com gorduras e resíduos oleosos."),
        ("Pluron Detaclor", "", "Limpeza manual ou espuma para pisos, paredes e utensílios."),
        ("Pluron 489 ATS", "", "Limpeza manual ou espuma para superfícies com gorduras e resíduos oleosos."),
        ("Pluron 428 A4", "", "Limpeza manual ou espuma para gorduras carbonizadas e resíduos oleosos."),
        ("Pluron 418 A", "", "Limpeza por espuma de superfícies com gorduras e resíduos de alimentos."),
        ("Pluron 446 A", "", "Limpeza de pisos e utensílios; não corrosivo para alumínio, cobre ou metais galvanizados."),
        ("Pluron 447 AE", "", "Limpeza por espuma de superfícies com gorduras e resíduos de alimentos."),
        ("Pluron 489 A", "", "Limpeza manual ou espuma para pisos, paredes e utensílios em indústrias alimentícias."),
        ("Pluron 490 A", "", "Remoção de sujidades inorgânicas em ambientes industriais."),
        ("Pluron 490 AM", "", "Remoção de sujidades inorgânicas, manchas de ferrugem e incrustações calcárias."),
        ("Pluron Acid Foam", "", "Limpeza externa em indústrias alimentícias, farmacêuticas e cosméticas."),
        ("Pluron 786 BS", "", "Aditivo para soluções cáusticas em sistemas CIP."),
        ("Pluron CE 800 B", "", "Antiespumante para sistemas CIP e máquinas de lavar."),
        ("Pluron 461 A1", "", "Desinfecção de equipamentos, tanques e tubulações."),
        ("Pluron 444 A", "", "Desinfecção manual por imersão ou circulação."),
        ("Pluron Hydroxysept", "", "Desinfecção de equipamentos, tanques e tubulações."),
        ("Pluron 463 AP", "", "Desinfecção de superfícies em indústrias alimentícias."),
        ("Pluron 464 A", "", "Desinfecção de superfícies, pisos, paredes e equipamentos (bactericida, fungicida e viricida)."),
     ]),

    # ============ 15. FARMACÊUTICA E HOSPITALAR ============
    ("Farmacêutica e Hospitalar",
     "Linha completa para o setor farmacêutico e hospitalar, em conformidade com as normas do Ministério da Saúde e ANVISA.",
     [
        ("Pluron 147 BG Sept Saúde", "", "Álcool 70% com clorexidina, pronto uso, antisséptico das mãos com emoliente."),
        ("Pluron Álcool Foam Saúde", "", "Antisséptico por espuma, sem necessidade de enxágue."),
        ("Pluron 147 AG Saúde", "", "Álcool gel 70% antisséptico das mãos."),
        ("Samprox 3,5%", "", "Esterilização de dialisadores, linhas de hemodiálise e desinfecção de alto nível de máquinas de hemodiálise."),
        ("Samprox 5%", "", "Esterilização de dialisadores, linhas de hemodiálise e desinfecção de alto nível de máquinas de hemodiálise."),
        ("Pluron Quater LH", "", "Desinfetante à base de Quaternário de 5ª geração e Biguanida para superfícies fixas e artigos não críticos; ação virucida testada pela UNICAMP."),
     ]),

    # ============ 16. AUTOMOTIVA ============
    ("Automotiva",
     "Linha automotiva: limpeza de chassis, carrocerias, motores e rodas até conservação geral de veículos.",
     [
        ("Mustang Silicone Gel", "", "Renova e revitaliza superfícies de borracha, vinil e plásticos do veículo."),
        ("Mustang Prima", "", "Renova superfícies emborrachadas como pneus e tapetes."),
        ("Pluron 7060 M Automotiva", "", "Sabonete para limpeza de graxas e óleos das mãos em oficinas."),
        ("Solumol 960 R", "", "Detergente para embelezamento automotivo; realça o brilho da pintura."),
        ("Supermix CR", "", "Lavagem manual ou automática de veículos e equipamentos com superfícies pintadas."),
        ("Mustang Azulão", "", "Limpeza super pesada para carrocerias de madeira, alumínio, chassis e motores."),
        ("Pollyclean E", "", "Limpeza de chassis, motores, rodas e caminhões com carroceria de madeira, baú e tanques pintados."),
        ("Supremix AT", "", "Limpeza de pisos, equipamentos de inox e alumínio, pátios de manobra e frotas."),
        ("Mustang Solumax DR 8", "", "Detergente desengraxante concentrado; remove graxas e resíduos betuminosos."),
        ("Pluron 7225 Automotiva", "", "Limpeza de chassis, motores, rodas e caminhões."),
     ]),

    # ============ 17. ACESSÓRIOS DE LIMPEZA ============
    ("Acessórios de Limpeza",
     "Materiais operacionais em Polipropileno, alumínio, microfibra e aço para rotinas profissionais.",
     [
        ("Espátula", "", "Limpador para box, janelas, frestas e fendas; cabo anatômico, acompanha 2 refis de microfibra."),
        ("Pá Coletora", "", "Com tampa e cabo de alumínio; trava na tampa para descarte seguro."),
        ("Pano de Microfibra", "", "Alta absorção; elimina poeira, sujeira e graxa, sem arranhar nem soltar fiapos."),
        ("Tela para Mictório", "", "Tela odorizadora com furos anti-respingos; fragrâncias Fruit-Fruit, Canela, Citrus e Algas."),
        ("Organizador para Cabos", "", "Mantém os cabos presos e otimiza o espaço; kits com 3, 4 e 6 suportes."),
        ("Placas Sinalizadoras", "", "Sinalizam e interditam áreas (piso molhado, cuidado, área em manutenção); material PEAD."),
        ("Pulverizadores", "", "Uso profissional, alta resistência química, gatilho ajustável; 500 ml e 1 L."),
        ("Balde 3 L", "", "Para limpeza geral e separação de resíduos; Polipropileno + ABS."),
        ("Balde 6 L", "", "Para limpeza geral e separação de resíduos; Polipropileno + ABS."),
        ("Balde 15 L Reforçado", "", "Graduação interna e bico dosador; 2 em 1 (balde + placa sinalizadora)."),
        ("Balde com Espremedor", "", "Espremedor super resistente com cabo de alumínio e manopla ergonômica."),
        ("Balde Due 30 L", "", "Divisão interna fixa com graduação; design arredondado e vibrante."),
        ("Rodízios (reposição)", "", "Para baldes e contentores."),
        ("Caixa Dobrável", "", "Montagem fácil com travamento no fundo; suporta 50 kg."),
        ("Cabos e Extensores", "", "Cabos telescópicos de 3M, 4,5M, 6M e 9M; cabo extensor de 1,40 m."),
        ("Lixeira 12 L Click", "", "Modelo Click (com tampa), com suporte para bobina de saco."),
        ("Lixeira 12 L Push", "", "Modelo Push (sem tampa), com suporte para bobina de saco."),
        ("Lixeira 15 L Porta Saco", "", "3 modelos: sem aro, com aro e aro + tampa."),
        ("Lixeira TVV 60 L", "", "Tampa basculante de ampla abertura, durabilidade e estabilidade."),
        ("Lixeira com Pedal 18 L", "", "Alta resistência, abertura máxima de 75°."),
        ("Lixeira com Pedal 36 L", "", "Alta resistência, abertura máxima de 75°."),
        ("Lixeira com Pedal 50 L", "", "Alta resistência, abertura máxima de 75°."),
        ("Lixeira 100 L", "", "Opção com rodas, alça de deslocamento e abertura de 85°."),
        ("Contentor 120 L", "", "Com rodas, ideal para coleta urbana, lixo hospitalar e resíduos industriais."),
        ("Contentor 240 L", "", "Duas rodas de 200 mm e design ergonômico."),
        ("Rodo de Borracha 35 cm", "", "Borracha dupla expandida de alta absorção."),
        ("Rodo de Borracha 45 cm", "", "Borracha dupla expandida de alta absorção."),
        ("Rodo de Borracha 55 cm", "", "Borracha dupla expandida de alta absorção."),
        ("Rodo de Borracha 65 cm", "", "Borracha dupla expandida de alta absorção."),
        ("Suporte para Mop Pó", "", "Com hastes metálicas flexíveis, ideal com cabo de 140 cm."),
        ("Suporte para Mop Úmido", "", "Haste em formato de presilha, fixação por rosca euro."),
        ("Suporte para Fibra", "", "Articulação que facilita a limpeza em locais de difícil acesso."),
        ("Suporte com Velcro", "", "Fixação rápida e prática para refis."),
        ("Suporte de Fibra com Alça", "", "Pega-mão anatômico para segurança em chapas quentes."),
        ("Refil para Mops", "", "Para mop úmido ou mop pó, em material de qualidade."),
        ("Mopinho 170 g", "", "Refil compacto para limpeza rápida."),
        ("Refil Mop Pó", "", "Refil para limpeza a seco."),
        ("Refil Mop Úmido 330 g", "", "Refil de maior gramatura para mop úmido."),
        ("Kit Balde Due", "", "Balde Due + placa sinalizadora + suporte de mop úmido + cabo + refil."),
        ("Kit Carro Funcional Pratic", "", "Balde Due + placa sinalizadora + carro funcional + suporte de mop + cabo + refil."),
        ("Kit Carro Funcional Titan", "", "Carro funcional titan com tampa + balde espremedor Due + placa sinalizadora + suportes de mop + cabos extensores + refis + pá coletora."),
        ("Kit Limpa Tudo (Limpeza Geral)", "", "Suporte fiber lock azul + fibra verde multiuso + fibra branca + cabo extensor 1,40 m."),
        ("Kit Mop Úmido Completo", "", "Suporte mop úmido + refil mop úmido ponta dobrada + cabo extensor 1,40 m."),
        ("Kit Mopinho", "", "Balde 15 L sinalizador + refil mopinho 170 g + espremedor."),
     ]),
]

class Command(BaseCommand):
    help = "Popula o catálogo HES com as 17 categorias e seus produtos (com códigos e descrições)."

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
            categoria, criada = Categoria.objects.get_or_create(
                nome=cat_nome,
                defaults={"descricao": cat_desc, "ativo": True},
            )
            if not criada and categoria.descricao != cat_desc:
                categoria.descricao = cat_desc
                categoria.save(update_fields=["descricao"])

            sub, _ = Subcategoria.objects.get_or_create(
                nome="Geral",
                categoria=categoria,
                defaults={"ativo": True, "ordem": 0},
            )

            for produto_nome, produto_codigo, produto_desc in produtos:
                obj, criado = Produto.objects.get_or_create(
                    nome=produto_nome,
                    subcategoria=sub,
                    defaults={
                        "codigo": produto_codigo,
                        "descricao": produto_desc,
                        "ativo": True,
                        "destaque": False,
                    },
                )
                if not criado:
                    mudou = False
                    if obj.descricao != produto_desc:
                        obj.descricao = produto_desc
                        mudou = True
                    if obj.codigo != produto_codigo:
                        obj.codigo = produto_codigo
                        mudou = True
                    if mudou:
                        obj.save(update_fields=["descricao", "codigo"])
                total += 1

            resumo.append((cat_nome, len(produtos)))

        self.stdout.write(self.style.SUCCESS(
            f"Seed concluído: {len(CATALOGO)} categorias e {total} produtos."
        ))
        for nome, qtd in resumo:
            self.stdout.write(f"  - {nome}: {qtd} produtos")