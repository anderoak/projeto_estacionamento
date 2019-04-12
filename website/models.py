from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=100)
    mensagem = models.TextField(max_length=100)

    def __str__(self):
        return self.nome


class HomePage(models.Model):
    linha1coluna1 = models.TextField(max_length=1000)
    linha1coluna2 = models.TextField(max_length=1000)
    linha2coluna1 = models.TextField(max_length=1000)
    linha2coluna2 = models.TextField(max_length=1000)
    linha3coluna1 = models.TextField(max_length=1000)
    linha3coluna2 = models.TextField(max_length=1000)

    def __str__(self):
        return "Texto da página 'Home'"


class ServicoPage(models.Model):
    textounico = models.TextField(max_length=3000)

    def __str__(self):
        return "Texto da página 'Serviços'"


class SobrePage(models.Model):
    linha1 = models.TextField(max_length=1000)
    linha2  = models.TextField(max_length=1000)

    def __str__(self):
        return "Texto da página 'Sobre'"


class PlanosPage(models.Model):
    linha1 = models.TextField(max_length=1000)
    linha2 = models.TextField(max_length=1000)

    def __str__(self):
        return "Texto da página 'Planos'"