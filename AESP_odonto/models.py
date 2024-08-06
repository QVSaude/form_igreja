from django.db import models

class AESP_odonto(models.Model):
    CONDICAO = models.CharField(max_length=1, default='1')
    NRO_CONTRATO = models.CharField(max_length=100)
    DATA_MOVIMENTO = models.DateTimeField()
    DATA_INICIO_UTILIZACAO = models.DateField()
    TIPO_CHOICES = [
        ('TI', 'Titular'),
    ]
    TIPO = models.CharField(max_length=2,  default='TI')
    NOME = models.CharField(max_length=255)
    NOME_MAE = models.CharField(max_length=255)
    DATA_NASCIMENTO = models.DateField()
    
    TIPO_LOGRADOURO_CHOICES = [
        (1, 'RUA'), (2, 'AVENIDA'), (3, 'ALAMEDA'), (4, 'TRAVESSA'), 
        (5, 'ACESSO'), (6, 'BALNEÁRIO'), (7, 'ESTRADA'), (8, 'FAZENDA'), 
        (9, 'SÍTIO'), (10, 'CHÁCARA'), (11, 'OUTRO'), (12, 'VIA'), 
        (13, 'PRAÇA'), (14, 'BOULEVARD'), (15, 'RODOVIA'), (16, 'QUADRA'), 
        (17, 'CONDOMINIO')
    ]
    TIPO_LOGRADOURO = models.IntegerField(choices=TIPO_LOGRADOURO_CHOICES)
    
    NOME_LOGRADOURO = models.CharField(max_length=255)
    NUMERO = models.CharField(max_length=10)
    BAIRRO = models.CharField(max_length=100)
    COMPLEMENTO = models.CharField(max_length=100, blank=True, null=True)
    CIDADE = models.CharField(max_length=100)
    ESTADO = models.CharField(max_length=2)
    CEP = models.CharField(max_length=8)
    RG = models.CharField(max_length=20)
    UF_RG = models.CharField(max_length=2)
    CPF = models.CharField(max_length=11)
    SEXO_CHOICES = [
        (1, 'Feminino'),
        (2, 'Masculino')
    ]
    SEXO = models.IntegerField(choices=SEXO_CHOICES)
    ESTADO_CIVIL_CHOICES = [
        (1, 'Amasiado(a)'), (2, 'Casado(a)'), (3, 'Divorciado(a)'), 
        (5, 'Separado(a)'), (6, 'Solteiro(a)'), (7, 'Viúvo(a)')
    ]
    ESTADO_CIVIL = models.IntegerField(choices=ESTADO_CIVIL_CHOICES)
    EMAIL = models.EmailField()
    DDD = models.CharField(max_length=2)
    FONE = models.CharField(max_length=10)
    CODIGOPLANODATASYS = models.CharField(max_length=20, default=196702)

class Dependente(models.Model):
    titular = models.ForeignKey(AESP_odonto, on_delete=models.CASCADE, related_name='dependentes')
    TIPO_CHOICES = [
        ('DE', 'Dependente')
    ]
    TIPO = models.CharField(max_length=2,  default='DE')
    NOME = models.CharField(max_length=255)
    NOME_MAE = models.CharField(max_length=255)
    DATA_NASCIMENTO = models.DateField()
    CPF_DEPENDENTE = models.CharField(max_length=11)
    
    SEXO_CHOICES = [
        (1, 'Feminino'),
        (2, 'Masculino')
    ]
    SEXO = models.IntegerField(choices=SEXO_CHOICES)
    
    ESTADO_CIVIL_CHOICES = [
        (1, 'Amasiado(a)'), (2, 'Casado(a)'), (3, 'Divorciado(a)'), 
        (5, 'Separado(a)'), (6, 'Solteiro(a)'), (7, 'Viúvo(a)')
    ]
    ESTADO_CIVIL = models.IntegerField(choices=ESTADO_CIVIL_CHOICES)
    
    GRAU_DEPENDENCIA_CHOICES = [
            ('2E', 'Esposa ou companheira'), 
            ('2C', 'Esposo ou companheiro'), 
            ('3M', 'Filhos'), 
            ('3F', 'Filhas'), 
            ('4M', 'Agregado masculino'), 
            ('4F', 'Agregado feminino'), 
            ('5P', 'Pai'), 
            ('5M', 'Mãe')
    ]
    GRAU_DEPENDENCIA = models.CharField(max_length=10, choices=GRAU_DEPENDENCIA_CHOICES)
    RG = models.CharField(max_length=20, blank=True, null=True)
    ORGAO_EMISSOR = models.CharField(max_length=100, blank=True, null=True)