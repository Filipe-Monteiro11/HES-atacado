from django.db import models

class Categoria(models.Model):
    nome = models.CharField('Nome', max_length=100, db_index=True)
    descricao = models.TextField('Descrição', blank=True)
    ordem = models.IntegerField('Ordem de exibição', default=0, db_index=True)
    ativo = models.BooleanField('Ativo', default=True, db_index=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['ordem', 'nome']

    def __str__(self):
        return self.nome

class Subcategoria(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        verbose_name='Categoria',
        related_name='subcategorias',
        db_index=True
    )
    nome = models.CharField('Nome', max_length=100, db_index=True)
    descricao = models.TextField('Descrição', blank=True)
    ordem = models.IntegerField('Ordem de exibição', default=0, db_index=True)
    ativo = models.BooleanField('Ativo', default=True, db_index=True)

    class Meta:
        verbose_name = 'Subcategoria'
        verbose_name_plural = 'Subcategorias'
        ordering = ['ordem', 'nome']
        indexes = [
            models.Index(fields=['categoria', 'ordem'], name='sub_cat_ordem_idx'),
            models.Index(fields=['categoria', 'ativo'], name='sub_cat_ativo_idx'),
        ]

    def __str__(self):
        return f'{self.categoria.nome} → {self.nome}'

class Produto(models.Model):
    subcategoria = models.ForeignKey(
        Subcategoria,
        on_delete=models.CASCADE,
        verbose_name='Subcategoria',
        related_name='produtos',
        db_index=True
    )
    codigo = models.CharField('Código', max_length=200, db_index=True)
    nome = models.CharField('Nome', max_length=200, db_index=True)
    descricao = models.TextField('Descrição', blank=True)
    imagem = models.ImageField(
        'Imagem',
        upload_to='produtos/',
        blank=True,
        null=True
    )
    destaque = models.BooleanField('Destaque na home', default=False, db_index=True)
    ativo = models.BooleanField('Ativo', default=True, db_index=True)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['subcategoria__ordem', 'nome']
        indexes = [
            models.Index(fields=['subcategoria', 'ativo'], name='prod_sub_ativ_idx'),
            models.Index(fields=['nome'], name='prod_nome_idx'),
            models.Index(fields=['destaque', 'ativo'], name='prod_dest_ativ_idx'),
        ]

    def __str__(self):
        return f'{self.codigo} — {self.nome}'