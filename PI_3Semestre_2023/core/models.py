from django.db import models

class DadosInstituicao(models.Model):
    id = models.IntegerField(primary_key=True)
    nome_instituicao = models.CharField('Nome_Instituição', max_length=100)
    cep = models.CharField('CEP', max_length=9)
    cnpj = models.CharField('CNPJ', max_length=14)
    rua = models.CharField('Rua', max_length=100)
    num = models.IntegerField('Número')
    bairro = models.CharField('Bairro', max_length=100)
    complemento = models.CharField('Complemento', max_length=100)
    cidade = models.CharField('Cidade', max_length=100)
    estado = models.CharField('Estado', max_length=2)
    tel = models.CharField('Telefone', max_length=25)
    cel = models.CharField('Celular', max_length=25)
    email = models.EmailField('Email', max_length=100)
    senha = models.CharField('Senha', max_length=100)
    descricao = models.CharField('Descricao', max_length=250)
    forma_ajuda1 = models.CharField('Forma_doacao1', max_length=150)
    forma_ajuda2 =  models.CharField('Forma_doacao2', max_length=150)
    forma_ajuda3 =  models.CharField('Forma_doacao3', max_length=150)
    latitude = models.CharField('Latitude', max_length=100)
    longitude = models.CharField('Longitude', max_length=100)
    data_hora_cadastro = models.DateTimeField('Data_Hora_Cadastro', auto_now_add=True)

class DadosUsuarios(models.Model):
    id = models.IntegerField(primary_key=True)
    nome_usuario = models.CharField('Nome_Usuário', max_length=100)
    cep = models.CharField('CEP', max_length=9)
    rua = models.CharField('Rua', max_length=100)
    num = models.IntegerField('Número')
    bairro = models.CharField('Bairro', max_length=100)
    cidade = models.CharField('Cidade', max_length=100)
    estado = models.CharField('Estado', max_length=2)
    data_hora_cadastro = models.DateTimeField('Data_Hora_Cadastro', auto_now_add=True)