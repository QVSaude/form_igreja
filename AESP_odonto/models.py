from django.db import models

class AESP_odonto(models.Model):
    CONDICAO = models.CharField(max_length=1, default='1')
    NRO_CONTRATO = models.CharField(max_length=100)
    DATA_MOVIMENTO = models.DateTimeField()
    DATA_INICIO_UTILIZACAO = models.DateTimeField()
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
    CEP = models.CharField(max_length=9)
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

    CODIGOPLANODATASYS_CHOICES = [('ROL_ANS', 'ROL ANS'),
    ('ROL_MAIS', 'ROL +'),
]

    CODIGOPLANODATASYS = models.CharField(max_length=20,choices=CODIGOPLANODATASYS_CHOICES)

    STATUS = models.CharField(max_length=20, default='Ativo', null=True)

    PASTOR_CHOICES = [
    ('ANDERSON INACIO DOS SANTOS', 'ANDERSON INACIO DOS SANTOS - ASSEMBLÉIA DE DEUS MINISTÉRIO FOGO E PALAVRA'),
    ('DALIELSON BERTO', 'DALIELSON BERTO – ASSEMBLÉIA DE DEUS MINISTÉRIO RESTAURANDO VIDAS'),
    ('ENOCK PESSOA DA SILVA', 'ENOCK PESSOA DA SILVA – ASSEMBLÉIA DE DEUS MINISTÉRIO GRAÇA E FAVOR'),
    ('RAUL OLIVEIRA DA SILVA', 'RAUL OLIVEIRA DA SILVA – ASSEMBLÉIA DE DEUS MINISTÉRIO REFÚGIO E FORTALEZA'),
    ('ISAIAS RABELO GONZAGA FILHO', 'ISAIAS RABELO GONZAGA FILHO – ASSEMBLÉIA DE DEUS MINISTÉRIO MISSÃO PARA CRISTO'),
    ('ANDRÉ LUIZ MOREIRA DE SOUZA', 'ANDRÉ LUIZ MOREIRA DE SOUZA – ASSEMBLÉIA DE DEUS MINISTÉRIO NOVA JERUSALÉM'),
    ('DAVID DE MOURA MIGUEL', 'DAVID DE MOURA MIGUEL – ASSEMBLEIA DE DEUS MINISTÉRIO NOVIDADE DE VIDA'),
    ('ANTONIO CARLOS RAYMUNDO DOS SANTOS', 'ANTONIO CARLOS RAYMUNDO DOS SANTOS – ASSEMBLÉIA DE DEUS MINISTÉRIO AO SOAR DA TROMBETA'),
    ('JOSÉ ROBERTO FERREIRA DE SOUZA', 'JOSÉ ROBERTO FERREIRA DE SOUZA - ASSEMBLÉIA DE DEUS MINISTÉRIO DE MÃOS DADAS NA PELEJA'),
    ('GERALDO SEBASTIÃO DA SILVA', 'GERALDO SEBASTIÃO DA SILVA – ASSEMBLÉIA DE DEUS MINISTÉRIO DEUS NO CONTROLE'),
    ('BRUNO PEREIRA DE SOUSA', 'BRUNO PEREIRA DE SOUSA – ASSEMBLÉIA DE DEUS MINISTÉRIO RESGATANDO ALMAS'),
    ('CELIO ROBERTO PAULINO AIRES', 'CELIO ROBERTO PAULINO AIRES – ASSEMBLÉIA DE DEUS MINISTÉRIO REMANESCENTE'),
    ('JERRY DOMINGUES DA SILVA', 'JERRY DOMINGUES DA SILVA – ASSEMBLÉIA DE DEUS MINISTÉRIO TEMPO DE COLHEITA'),
    ('JOÃO CARLOS DE JESUS', 'JOÃO CARLOS DE JESUS – ASSEMBLÉIA DE DEUS MINISTÉRIO ERGUER'),
    ('JOÃO HUMBERTO OLIVEIRA SANTOS', 'JOÃO HUMBERTO OLIVEIRA SANTOS – ASSEMBLÉIA DE DEUS MINISTÉRIO ELE VIRÁ'),
    ('MARCILON DE FIGUEIREDO DOS SANTOS', 'MARCILON DE FIGUEIREDO DOS SANTOS - ASSEMBLÉIA DE DEUS MINISTÉRIO COLUNA DE BETEL'),
    ('LINDON JHONSON', 'LINDON JHONSON – ASSEMBLÉIA DE DEUS MINISTÉRIO NASCER EM CRISTO'),
    ('MARISTELA FERREIRA DA SILVA', 'MARISTELA FERREIRA DA SILVA – ASSEMBLEIA DE DEUS MINISTÉRIO SHEKINAH'),
    ('PAULO CEZAR ROCHA DE MELLO', 'PAULO CEZAR ROCHA DE MELLO – ASSEMBLÉIA DE DEUS MINISTÉRIO RESTAURANDO VIDAS EM JESUS'),
]

    PASTOR = models.CharField(max_length=200, choices=PASTOR_CHOICES, null=True)


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
    STATUS = models.CharField(max_length=20, default='Ativo', null=True)