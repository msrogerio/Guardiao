from django.db import models

class UsuarioSistema(models.Model):

    POSTO_GRADUACAO_CHOICE = (
        ('Cel', 'Coronel'),
        ('Ten-Cel', 'Tenente-Coronel'),
        ('Maj', 'Major'),
        ('Cap', 'Capitão'),
        ('1º Ten', '1º Tenente'),
        ('2º Ten', '2º Tenente'),
        ('As-Of', 'Apirante'),
        ('Al-Of', 'Aluno-Oficial'),
        ('Al-CHOA', 'Aluno-CHOA'),
        ('St', 'Subtenente'),
        ('1º Sgt', '1º Sargento'),
        ('Al-CAS', 'Aluno-CAS'),
        ('2º Sgt', '2º Sargento'),
        ('3º Sgt', '3º Sargento'),
        ('Al-CFS', 'Aluno-CFS'),
        ('Cb', 'Cabo'),
        ('Al-Cb', 'Aluno-Cabo'),
        ('Sd', 'Soldado'),
        ('Al-Sd', 'Aluno-Soldado'),
    )

    TIPO_USUARIO_CHOICE = (
        (1, 'Básico'),
        (2, 'Analista'),
        (3, 'Administador')
    )

    nome_completo = models.CharField(max_length=50, blank=True, null=True)
    
    """ Limita campo pelo choice POSTO_GRADUACAO_CHOICE """
    posto_graduacao = models.CharField(choices = POSTO_GRADUACAO_CHOICE, max_length=50, blank=True, null=True)
    matricula = models.IntegerField(blank=True, null=True)
    rg_pm = models.CharField(max_length=50, blank=True, null=True)
    cpf = models.CharField(max_length=50, blank=True, null=True)
    lotacao = models.CharField(max_length=50, blank=True, null=True)
    
    """ Limita campoa pelo Choice TIPO_USUARIO_CHOICE """
    tipo_usuario = models.IntegerField(choices = TIPO_USUARIO_CHOICE, blank=True, null=True)
    
    def __str__(self):
        return self.nome_completo + ' ' + self.posto_graduacao + ' PM' 


class LogUsuarioSistema(models.Model):
    usuario = models.ForeignKey(UsuarioSistema, blank=True, on_delete=False)
    acao_sistema = models.CharField(max_length=350, blank=True, null=True)
    data_log = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.acao_sistema