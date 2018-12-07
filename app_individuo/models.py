from django.db import models

def uploadPasta(instance, filename):
    return '{0}/{1}'.format(instance.Individuo.cpf, filename)

""" (block endereço) """
class Bairro(models.Model):
    nome_bairro = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.nome_bairro    

class Conjunto(models.Model):
    nome_conjunto = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.nome_conjunto    

class Endereco(models.Model):
    rua = models.CharField(max_length=250, null=True, blank=True)
    numero = models.IntegerField(null=True, blank=True)
    
    """ 1,n """
    quadra = models.CharField(max_length=4, blank=True, null=True)

    """ 1,n """
    bairro = models.ForeignKey(Bairro, blank=True, on_delete=False)
    complemento = models.TextField(blank=True, null=True)
    #complemento

    def __str__(self):
        return self.rua

""" (endblock endereços) """

"""
*
*
*
*
"""
class DocumentosUnico(models.Model):
    cpf = models.CharField(max_length=14, null=True, blank=True)
    numero_habilitacao = models.IntegerField(null=True, blank=True)
    categoria = models.CharField(max_length=50, null=True, blank=True)    
    numero_carteira_trabalho = models.IntegerField(null=True, blank=True)
    rg = models.CharField(max_length=9, null=True, blank=True)
    orgao_expedidor = models.CharField(max_length=5, blank=True, null=True)
    uf = models.CharField(max_length=2, null=True, blank=True)
    
    def __str__(self):
        return self.cpf

class Imagen(models.Model):
    imagens = models.ImageField(upload_to=uploadPasta, height_field=None, width_field=None, max_length=None, null=True, blank=True)
    cpf = models.OneToOneField(DocumentosUnico, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.cpf
    

class Tatuagem(models.Model):
    tatuagem = models.ImageField(upload_to=uploadPasta, height_field=None, width_field=None, max_length=None, null=True, blank=True)
    cpf = models.OneToOneField(DocumentosUnico, on_delete=models.CASCADE)
    descricao_tatuagem = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.descricao_tatuagem
    
class Caracteristicas(models.Model):
    COR_PELE_CHOICES = (
        ('Branca', 'Branca'),
        ('Parda', 'Parda'),
        ('Negra', 'Negra'),
        ('Amarela', 'Amarela')
    )
    
    COR_OLHOS_CHOICES = (
        ('Azuis', 'Azuis'),
        ('Verdes', 'Verdes'),
        ('Casatanhos', 'Castanhos'),
        ('Pretos', 'Pretos')
    )

    COR_CABELO_CHOICES = (
        ('Pretos', 'Pretos'),
        ('Castanhos-escuro', 'Castanhos-escuro'),
        ('Castanhos-claro', 'Castanhos-claro'),
        ('Loiros', 'Loiros'),
        ('Ruivos', 'Ruivos'),
        ('Outros', 'Outros'),
    )

    TIPO_CABELO_CHOICES = (
        ('Liso', 'Liso'),
        ('Ondulado', 'Ondulado'),
        ('Encaracolado', 'Encaracolado'),
        ('Crespo', 'Crespo'),
    )

    altura = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    peso = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    cor_pele = models.CharField(choices=COR_PELE_CHOICES, max_length=50, blank=True, null=True)
    cor_olho = models.CharField(choices=COR_OLHOS_CHOICES, max_length=50, blank=True, null=True)
    cor_cabelo = models.CharField(choices=COR_CABELO_CHOICES, max_length=50, blank=True, null=True)
    tipo_cabelo = models.CharField(choices=TIPO_CABELO_CHOICES, max_length=50, blank=True, null=True)
    marcas_endemica = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.marcas_endemica
    

class Individuo(models.Model):
    nome_completo = models.CharField(max_length=50, null=True, blank=True)
    alcunha = models.CharField(blank=True, null=True, max_length=50)
    data_nascimento = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    nome_mae = models.CharField(max_length=50, null=True, blank=True)
    nome_pai = models.CharField(max_length=50, null=True, blank=True)
    naturalidade = models.CharField(max_length=50, blank=True, null=True)
    nacionalidade = models.CharField(max_length=50, null=True, blank=True)
    profissao = models.CharField(max_length=50, null=True, blank=True)
    faccao = models.CharField(max_length=50, null=True, blank=True)
    
    "1,1 - Individuo ligado a um único Documento unico"  
    documento_unico = models.OneToOneField(DocumentosUnico, blank=True, on_delete=False)
    
    endereco = models.ManyToManyField(Endereco, blank=True)

    caracteristicas = models.OneToOneField(Caracteristicas, blank=True, on_delete=False)

    tatuagem = models.ManyToManyField(Tatuagem, blank=True)

    imagem = models.ManyToManyField(Imagen, blank=True)

    def __str__(self):
        return self.nome_completo
