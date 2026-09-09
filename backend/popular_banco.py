import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from produtos.models import Categoria, Subcategoria, Produto

# Limpar dados antigos
Produto.objects.all().delete()
Subcategoria.objects.all().delete()
Categoria.objects.all().delete()

print('Limpando banco... OK')

# ============================================
# 1. DISPENSERS — LINHA GOLD
# ============================================
cat1 = Categoria.objects.create(
    nome='Dispensers — Linha Gold',
    descricao='Linha premium de dispensers com design sofisticado.',
    ordem=1,
)
subs_gold = [
    ('Dispenser Sabonete Espuma', 'DSE05'),
    ('Dispenser Sabonete Líquido', 'DSE10'),
    ('Dispenser Papel Toalha Bobina', 'DPB6300'),
    ('Dispenser Papel Toalha Interfolhado', 'DPI2400'),
    ('Dispenser Papel Toalha Interfolhado Mini', 'DPIM1400'),
    ('Dispenser Coletor de Absorvente', 'DCA1000'),
    ('Dispenser Guardanapeira Interfolhada', 'DG8000'),
    ('Dispenser Assento Sanitário', 'DCS1000'),
    ('Dispenser Papel Higiênico', 'DHI8000'),
    ('Dispenser Papel Higiênico Bobina', 'DPHB8200 / DPHB1620'),
]

# ============================================
# 2. DISPENSERS — LINHA CARE
# ============================================
cat2 = Categoria.objects.create(
    nome='Dispensers — Linha Care',
    descricao='Design suave e funcional para hospitais, clínicas e ambientes institucionais.',
    ordem=2,
)
subs_care = [
    ('Dispenser Sabonete Espuma', 'DPH-107'),
    ('Dispenser Sabonete Líquido', 'DPH-108'),
    ('Dispenser Papel Toalha Bobina', 'DPH-101'),
    ('Dispenser Papel Toalha Interfolhado', 'DPH-102'),
    ('Dispenser Papel Toalha Interfolhado Mini', 'DPH-103'),
    ('Dispenser Papel Higiênico', 'DPH-104 / DPH-105 / DPH-106'),
    ('Dispenser Coletor de Absorvente', 'DPH-109'),
    ('Dispenser Guardanapeira Interfolhada', 'DPH-110'),
    ('Dispenser Assento Sanitário', 'DPH-111'),
]

# ============================================
# 3. DISPENSERS — LINHA STANDARD
# ============================================
cat3 = Categoria.objects.create(
    nome='Dispensers — Linha Standard',
    descricao='Funcionalidade e durabilidade em design versátil.',
    ordem=3,
)
subs_standard = [
    ('Dispenser Sabonete Líquido', 'ELT-2105'),
    ('Dispenser Sabonete Espuma', 'ELT-2106'),
    ('Dispenser Papel Toalha Bobina', 'ELT-2101'),
    ('Dispenser Papel Toalha Interfolhado', 'ELT-2102'),
    ('Dispenser Papel Toalha Interfolhado Mini', 'ELT-2103'),
    ('Dispenser Papel Higiênico', 'ELT-2104'),
    ('Dispenser Coletor de Absorvente', 'ELT-2107'),
    ('Dispenser Guardanapeira Interfolhada', 'ELT-2108'),
    ('Dispenser Assento Sanitário', 'ELT-2109'),
]

# ============================================
# 4. EQUIPAMENTOS PROFISSIONAIS
# ============================================
cat4 = Categoria.objects.create(
    nome='Equipamentos Profissionais',
    descricao='Sistemas de limpeza profissional — equipamentos industriais e comerciais.',
    ordem=4,
)
subs_equip = [
    ('Diluidores (Sistema Venturi)', 'Dosimax / Lawdy / BOHDOZ / TRON'),
    ('Dosadores Individuais', 'Máquinas de lavar louça e lavanderias'),
    ('Treinamentos de Uso', 'Produtos e equipamentos'),
]

# ============================================
# 5. PAPÉIS INSTITUCIONAIS
# ============================================
cat5 = Categoria.objects.create(
    nome='Papéis Institucionais',
    descricao='Linha de papéis para uso institucional — papel toalha e higiênico.',
    ordem=5,
)
subs_papeis = [
    ('Toalha Bobina 200M', 'PTB8200 (6 x 200M)'),
    ('Toalha Bobina 150M', 'PTB8150 (6 x 150M)'),
    ('Toalha Interfolhada 2 Dobras', 'PTI1250 (8.000 fls)'),
    ('Toalha Interfolhada 3 Dobras', 'PTI12400 (2.400 fls)'),
    ('Higiênico Bobina Folha Dupla', 'PHBD8300 (8 rolos)'),
    ('Higiênico Bobina Folha Simples', 'PHB8300'),
    ('Higiênico Interfolhado Folha Dupla', 'PHCLFD20X10/8000 (8.000 fls)'),
    ('Higiênico Interfolhado', 'IHI12 (12.000 fls)'),
]

# ============================================
# 6. HIGIENE PESSOAL INSTITUCIONAL
# ============================================
cat6 = Categoria.objects.create(
    nome='Higiene Pessoal Institucional',
    descricao='Sabonetes, antissépticos e álcoois para higiene institucional.',
    ordem=6,
)
subs_higiene = [
    ('Pluron Clorexidine', 'Antisséptico'),
    ('Pluron Handmax Erva Doce', 'Sabonete perfumado'),
    ('Pluron Handmax Blue', 'Perfume floral'),
    ('Pluron Foam Hand Sept', 'Limpeza e assepsia das mãos'),
    ('Pluron Handfoam', 'Aplicação por espuma'),
    ('Pluron 144 A Sept', 'Com triclosan'),
    ('Pluron 147 AG', 'Álcool gel 70% antisséptico'),
    ('Pluron Álcool Foam', 'Antisséptico por espuma, sem enxágue'),
    ('Pluron 147 BG Sept', 'Álcool 70% com clorexidina'),
]

# ============================================
# 7. TRATAMENTO DE PISO
# ============================================
cat7 = Categoria.objects.create(
    nome='Tratamento de Piso',
    descricao='Produtos para limpeza, selagem e enceramento de pisos.',
    ordem=7,
)
subs_piso = [
    ('Pluron 7215', 'Limpeza de pisos de mármore, borracha, cerâmica'),
    ('Pluron 7225', 'Remoção de ceras de pisos porosos'),
    ('Pluron 7230', 'Limpeza de pisos, paredes, caixas plásticas'),
    ('Pluron Top Remove', 'Removedor de ceras e sujidades'),
    ('Pluron Selafix', 'Base seladora antiderrapante interna'),
    ('Pluron Selafix Ex', 'Base seladora interna e externa'),
    ('Pluron Maxbrilho AT', 'Cera auto brilho impermeabilizante'),
    ('Pluron Top Brilho', 'Cera auto brilho 3x1 (sela, brilho, protege)'),
    ('Pluron 7914', 'Cera auto brilho para pisos laváveis'),
]

# ============================================
# 8. LIMPADORES PERFUMADOS / ODORIZANTES
# ============================================
cat8 = Categoria.objects.create(
    nome='Limpadores Perfumados / Odorizantes',
    descricao='Limpadores perfumados e odorizantes para ambientes.',
    ordem=8,
)
subs_limpadores = [
    ('Pluron Trioxy', 'Peróxido de hidrogênio, limpeza geral'),
    ('Pluron Limpador Capim Limão', 'Limpador perfumado'),
    ('Pluron Limpador Pitanga', 'Limpador perfumado'),
    ('Pluron Multi Citronela', 'Afasta insetos'),
    ('Pluron Multi Porcelanato', 'Limpador de porcelanato'),
    ('Pluron H8 Premium', 'Elimina cheiro de tabaco/odorizante'),
    ('Pluron H3 Herbal', 'Odorizante'),
    ('Pluron H2 Premium', 'Odorizante'),
    ('Pluron H4 Marine', 'Odorizante'),
    ('Pluron H5 Premium', 'Odorizante'),
    ('Pluron H4 Premium', 'Odorizante'),
]

# ============================================
# 9. DESINFETANTES PERFUMADOS
# ============================================
cat9 = Categoria.objects.create(
    nome='Desinfetantes Perfumados',
    descricao='Desinfetantes com ativos bactericidas e limpadores de superfícies.',
    ordem=9,
)
subs_desinfetantes = [
    ('Pluron 7470', 'Limpeza de vidros, espelhos, acrílicos'),
    ('Pluron Sanit Eucalipto', 'Desinfetante perfumado'),
    ('Pluron Sanit Floral', 'Desinfetante perfumado'),
    ('Pluron Sanit Floral Fresh', 'Desinfetante perfumado'),
    ('Pluron Sanit Intense Floral', 'Desinfetante perfumado'),
    ('Pluron Sanit Intense Summer', 'Desinfetante perfumado'),
    ('Pluron Sanit Intense Marine', 'Desinfetante perfumado'),
    ('Pluron Sanit Lavanda', 'Desinfetante perfumado'),
    ('Pluron Sanit Marine', 'Desinfetante perfumado'),
    ('Pluron Sanit Top Floral', 'Desinfetante perfumado'),
    ('Pluron Sanit Top Lavanda', 'Desinfetante perfumado'),
    ('PollYclean 10.000', 'Limpador de vasos sanitários'),
]

# ============================================
# 10. DESINCRUSTANTES / LIMPA ALUMÍNIO
# ============================================
cat10 = Categoria.objects.create(
    nome='Desincrustantes / Limpa Alumínio',
    descricao='Produtos para desincrustação, desengorduramento e limpeza de alumínio.',
    ordem=10,
)
subs_desincrustantes = [
    ('Pluron 7160', 'Lavar e desengordurar pisos, fogões, exaustores'),
    ('Pluron 7710 AE', 'Limpeza por espuma de gorduras carbonizadas'),
    ('Pluron 236 A', 'Desincrustação de formas, latões, garrafas'),
    ('Pluron 7756', 'Higienização de utensílios em máquinas de lavar'),
    ('Pluron 7888', 'Desinfetante para frutas, legumes e verduras'),
    ('Pluron 7799 A', 'Enxágue final de máquinas de lavar louças'),
    ('Pluron Versat', 'Limpeza de depósitos de gorduras carbonizadas'),
    ('Pluron La 21', 'Detergente ácido para alumínio'),
]

# ============================================
# 11. COZINHA INDUSTRIAL E RESTAURANTES
# ============================================
cat11 = Categoria.objects.create(
    nome='Cozinha Industrial e Restaurantes',
    descricao='Produtos para limpeza de cozinhas industriais, restaurantes e utensílios.',
    ordem=11,
)
subs_cozinha = [
    ('Pluron Top Grill', 'Limpeza de fornos, grelhas, chapas e gordura carbonizada'),
    ('Detergente Neutro Pluron 194 A', 'Detergente neutro'),
    ('Detergente Neutro Pluron 194 AV', 'Detergente neutro'),
    ('Pluron 404 A', 'Limpeza de utensílios, pisos, louças'),
    ('Pluron 406 A', 'Limpeza de utensílios, pisos, louças'),
    ('Pluron Maq Duo', '2x1 lavagem e secagem'),
    ('Pluron Maq Det', 'Lavagem de máquinas de lavar louça'),
    ('Pluron Maq Sec', 'Secagem de máquinas de lavar louça'),
    ('Pluron Maq Clor', 'Cloração em máquinas de lavar louça'),
]

# ============================================
# 12. LATICÍNIOS
# ============================================
cat12 = Categoria.objects.create(
    nome='Laticínios',
    descricao='Produtos para limpeza de ordenhadeiras, CIP, tanques e indústrias de laticínios.',
    ordem=12,
)
subs_laticinios = [
    ('Pluron Alcali Clor', 'Limpeza de ordenhadeiras e CIP com cloro'),
    ('Pluron ClorcIP', 'Limpeza CIP com circuito post mix e chopeiras'),
    ('Pluron 426 A', 'Limpeza manual/circulação em indústrias'),
    ('Pluron 950 Pack', 'Lubrificação de esteiras'),
    ('Pluron 327 AS', 'Limpeza por circulação (CIP)'),
    ('Pluron 327 CIP', 'Limpeza por circulação (CIP)'),
    ('Pluron Nitric', 'Detergente ácido para pasteurizadores'),
    ('Pluron 320 A', 'Limpeza ácida de tanques de cerveja'),
    ('Pluron 418 A', 'Limpeza por espuma'),
    ('Pluron 446 A', 'Limpeza por espuma'),
    ('Pluron 447 AE', 'Desengraxantes por espuma'),
    ('Pluron 489 A', 'Desengraxantes por espuma'),
    ('Pluron 490 A', 'Remoção de sujidades inorgânicas'),
    ('Pluron 490 AM', 'Remoção de sujidades inorgânicas'),
    ('Pluron Acid Foam', 'Detergente ácido para indústrias alimentícias'),
    ('Pluron 786 B5', 'Aditivo para soluções cáusticas e CIP'),
    ('Pluron CE 800 B', 'Aditivo para soluções cáusticas e CIP'),
    ('Pluron 461 A1', 'Desinfetante'),
    ('Pluron 463 AP', 'Desinfetante'),
    ('Pluron 464 A', 'Desinfetante'),
    ('Pluron 444 A', 'Desinfetante'),
    ('Pluron Hidroxysept', 'Desinfetante'),
]

# ============================================
# 13. FRIGORÍFICOS E ABATEDOUROS
# ============================================
cat13 = Categoria.objects.create(
    nome='Frigoríficos e Abatedouros',
    descricao='Produtos para limpeza e desinfecção em frigoríficos e abatedouros.',
    ordem=13,
)
subs_frigorificos = [
    ('Pluron 199 A1', 'Tratamento de ganchos e carretilhas'),
    ('Pluron 199 A2', 'Tratamento de ganchos e carretilhas'),
    ('Pluron 337 AB', 'Limpeza de ganchos, garrafas e circulação'),
    ('Pluron 488 A', 'Limpeza por imersão de cozinhadores'),
    ('Pluron 484 A', 'Detergente alcalino'),
    ('Pluron 485 A', 'Detergente alcalino'),
    ('Pluron 485 A SE', 'Detergente alcalino'),
    ('Pluron 485 AE', 'Detergente alcalino'),
    ('Pluron CloroFoam Al', 'Alcalino clorado espumante'),
    ('Pluron Detaclor', 'Alcalino clorado espumante'),
    ('Pluron Álcool Sept 15%', 'Limpeza e desinfecção em uma etapa'),
]

# ============================================
# 14. SUPERMERCADOS
# ============================================
cat14 = Categoria.objects.create(
    nome='Supermercados',
    descricao='Produtos para limpeza e higienização de supermercados.',
    ordem=14,
)
subs_supermercados = [
    ('Pluron 7160', 'Lavar e desengordurar pisos'),
    ('Pluron Top Grill', 'Limpeza de fornos e superfícies'),
    ('Pluron Det Clean', 'Lavagem de utensílios e equipamentos'),
    ('Pluron Detaclor', 'Limpeza por espuma com cloro'),
    ('Pluron 144 A Sept', 'Sabonete antisséptico com triclosan'),
    ('Pluron 444 A', 'Desinfetante'),
    ('Pluron 461 A', 'Desinfetante'),
    ('Pluron 464 A', 'Desinfetante'),
]

# ============================================
# 15. LAVANDERIA
# ============================================
cat15 = Categoria.objects.create(
    nome='Lavanderia',
    descricao='Perfume, maciez, alvejantes, desinfetantes e detergentes para lavanderia.',
    ordem=15,
)
subs_lavanderia = [
    ('Pluron Soft Premium', 'Amaciante 2 em 1'),
    ('Pluron Soft Intense', 'Amaciante 2 em 1'),
    ('Pluron 909 LC', 'Amaciante 2 em 1'),
    ('Pluron 835 LL', 'Amaciante 2 em 1'),
    ('Pluron Passe Pronto', 'Engomadoria/perfume'),
    ('Pluron 836 LL', 'Alvejante e desinfetante'),
    ('Pluron 920 LL4', 'Alvejante e desinfetante'),
    ('Pluron 960 L', 'Alvejante e desinfetante'),
    ('Pluron Maxclor', 'Alvejante e desinfetante'),
    ('Pluron 985 L', 'Acidulante e anticloro'),
    ('Pluron 834 LL', 'Detergente e umectante'),
    ('Pluron 888 LLO', 'Detergente e umectante'),
    ('Pluron Max Detergente em Pó', 'Detergente e umectante'),
    ('Pluron 327 CIP', 'Detergente e umectante'),
    ('Pluron 961 L', 'Detergente e umectante'),
    ('Pluron 962 L', 'Detergente e umectante'),
    ('Pluron 949 L', 'Detergente e umectante'),
    ('Pluron Iniby Lav', 'Detergente e umectante'),
    ('Pluron Cloth Wash', 'Lavanderia'),
    ('Pluron Cloth Wash White', 'Lavanderia'),
    ('Pluron Coco Lava Roupas', 'Lavanderia'),
    ('Pluron Detacid L', 'Lavanderia'),
    ('Pluron Lav Solv', 'Lavanderia'),
    ('Pluron Lav Clean', 'Lavanderia'),
    ('Pluron 833 LL', 'Lavanderia'),
    ('Pluron Alcalav', 'Lavanderia'),
    ('Pluron 911 LLX', 'Lavanderia'),
    ('Pluron 837 LL3', 'Lavanderia'),
    ('Pluron 847 LLF', 'Lavanderia'),
    ('Pluron 964 L', 'Lavanderia'),
]

# ============================================
# 16. FARMACÊUTICA E HOSPITALAR
# ============================================
cat16 = Categoria.objects.create(
    nome='Farmacêutica e Hospitalar',
    descricao='Produtos para esterilização e desinfecção hospitalar.',
    ordem=16,
)
subs_farma = [
    ('Samprox 3,5%', 'Esterilização de dialisadores e hemodiálise'),
    ('Samprox-H 3,5%', 'Esterilização de dialisadores e hemodiálise'),
    ('Samprox 5%', 'Esterilização de dialisadores'),
    ('Samprox-H 5%', 'Esterilização de dialisadores'),
    ('Pluron Quater LH', 'Desinfetante à base de quaternário de amônio'),
    ('Pluron 147 BG Sept Saúde', 'Álcool 70% com clorexidina'),
    ('Pluron Álcool Foam Saúde', 'Antisséptico por espuma'),
    ('Pluron 147 AG Saúde', 'Álcool em gel 70%'),
]

# ============================================
# 17. AUTOMOTIVA
# ============================================
cat17 = Categoria.objects.create(
    nome='Automotiva',
    descricao='Shampoos, detergentes e recuperadores automotivos.',
    ordem=17,
)
subs_automotiva = [
    ('Solumol 960 R', 'Detergente de embelezamento'),
    ('Supermix Cr', 'Lavagem manual ou automática'),
    ('Mustang Azulão', 'Limpeza super pesada'),
    ('PollYclean E', 'Limpeza de chassis, motores, rodas'),
    ('Supremix At', 'Limpeza de pisos e frotas'),
    ('Mustang Solumax Dr 8', 'Desengraxante concentrado'),
    ('Mustang Silicone Gel', 'Renova borracha, vinil e plásticos'),
    ('Mustang Prima', 'Renova pneus e tapetes'),
    ('Pluron 7060 M', 'Sabonete para as mãos — graxas e óleos'),
    ('Pluron 7225', 'Limpeza de pisos'),
]

# ============================================
# 18. ACESSÓRIOS DE LIMPEZA
# ============================================
cat18 = Categoria.objects.create(
    nome='Acessórios de Limpeza',
    descricao='Acessórios e utensílios para limpeza profissional.',
    ordem=18,
)
subs_acessorios = [
    ('Espátula Limpa Vidros', 'Com 2 refis de microfibra'),
    ('Pá Coletora', 'Com tampa e trava'),
    ('Pano Microfibra', 'Kits com 4, 6 e 12'),
    ('Organizador para Cabos', 'Acessório'),
    ('Tela para Mictório', 'Fragrâncias: fruit-fruit, canela, citrus, algas'),
    ('Placas Sinalizadoras', 'Piso molhado, manutenção, não entre'),
    ('Pulverizadores 1L', '1 litro'),
    ('Pulverizadores 500ml', '500ml'),
    ('Baldes 3L', 'Balde 3 litros'),
    ('Baldes 6L', 'Balde 6 litros'),
    ('Balde 15L Reforçado', 'Balde 15 litros reforçado'),
    ('Balde com Espremedor', 'Balde com espremedor'),
    ('Balde Due 30L', 'Balde 30 litros'),
    ('Kit para Carro Funcional', 'Kit de limpeza'),
    ('Cabos Extensores Telescópicos', '1,40m a 9m'),
    ('Caixa Dobrável', 'Acessório'),
    ('Lixeiras 12L', 'Lixeira 12 litros'),
    ('Lixeiras 15L porta saco', 'Lixeira 15 litros porta saco'),
    ('Lixeiras 18L com pedal', 'Lixeira 18 litros com pedal'),
    ('Lixeiras 36L com pedal', 'Lixeira 36 litros com pedal'),
    ('Lixeiras 50L com pedal', 'Lixeira 50 litros com pedal'),
    ('Lixeiras 60L TVV', 'Lixeira 60 litros TVV'),
    ('Lixeiras 100L', 'Lixeira 100 litros'),
    ('Contentor 120L', 'Contentor 120 litros'),
    ('Contentor 240L', 'Contentor 240 litros'),
    ('Rodos de borracha preta', '35 a 65 cm'),
    ('Rodos de borracha branca', '35 a 65 cm'),
    ('Suportes para mop pó', 'Suporte'),
    ('Suportes para mop úmido', 'Suporte'),
    ('Suportes para fibra', 'Suporte'),
    ('Refis para Mop úmido 330g', 'Refil mop úmido 330g'),
    ('Refis para Mopinho 170g', 'Refil mopinho 170g'),
    ('Kit Limpa Tudo', 'Kit de limpeza'),
    ('Kit Mop Úmido Completo', 'Kit de limpeza'),
    ('Kit Mopinho', 'Kit de limpeza'),
    ('Kit Limpeza Completa', 'Kit de limpeza'),
]

# ============================================
# CRIAR SUBCATEGORIAS E PRODUTOS
# ============================================
dados = [
    (cat1, subs_gold),
    (cat2, subs_care),
    (cat3, subs_standard),
    (cat4, subs_equip),
    (cat5, subs_papeis),
    (cat6, subs_higiene),
    (cat7, subs_piso),
    (cat8, subs_limpadores),
    (cat9, subs_desinfetantes),
    (cat10, subs_desincrustantes),
    (cat11, subs_cozinha),
    (cat12, subs_laticinios),
    (cat13, subs_frigorificos),
    (cat14, subs_supermercados),
    (cat15, subs_lavanderia),
    (cat16, subs_farma),
    (cat17, subs_automotiva),
    (cat18, subs_acessorios),
]

total_cats = 0
total_subs = 0
total_prods = 0

for categoria, subcats in dados:
    total_cats += 1
    for i, (nome_sub, codigo) in enumerate(subcats):
        sub, created = Subcategoria.objects.get_or_create(
            categoria=categoria,
            nome=nome_sub,
            defaults={'descricao': codigo, 'ordem': i + 1}
        )
        if created:
            total_subs += 1
        
        # Garantir código único
        codigo_unico = codigo
        contador = 1
        while Produto.objects.filter(codigo=codigo_unico).exists():
            codigo_unico = f'{codigo} ({contador})'
            contador += 1
        
        produto, created = Produto.objects.get_or_create(
            codigo=codigo_unico,
            defaults={
                'subcategoria': sub,
                'nome': nome_sub,
                'descricao': categoria.descricao,
                'destaque': False,
                'ativo': True,
            }
        )
        if created:
            total_prods += 1

print(f'✅ {total_cats} categorias criadas!')
print(f'✅ {total_subs} subcategorias criadas!')
print(f'✅ {total_prods} produtos criados!')
print('✅ Banco populado com sucesso!')
