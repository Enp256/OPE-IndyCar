from django.db import models
from django.urls import reverse 
# Create your models here.

class Customer(models.Model):
    nome = models.CharField(max_length=60)
    endereco = models.CharField(max_length=100)
    bairro = models.CharField(max_length=30)
    email = models.EmailField(max_length=60)
    telefone = models.IntegerField()

    def __str__(self):
        return self.nome


class Cliente(Customer):
    cpf = models.CharField(max_length=12)

    def get_editar_cliente(self):
        return reverse('editar_cliente',kwargs={'id':self.id})
    def get_del_cliente(self):
        return reverse('deletar_cliente',kwargs={'id':self.id})


class Empresa(Customer):
    cnpj = models.CharField(max_length=14)

    def get_editar_empresa(self):
        return reverse('editar_empresa',kwargs={'id':self.id})
    def get_del_empresa(self):
        return reverse('deletar_empresa',kwargs={'id':self.id})




class OrdemDeServico(models.Model):
    cliente = models.ForeignKey(Customer,on_delete=models.PROTECT)
    marca_veiculo = models.CharField(max_length=10)
    modelo_veiculo = models.CharField(max_length=20)
    cor_veiculo = models.CharField(max_length=10)
    ano_veiculo = models.SmallIntegerField()
    placa_veiculo = models.CharField(max_length=7)
    cidade_veiculo = models.CharField(max_length=10)
    estado_veiculo = models.CharField(max_length=2)
    reparos_necessarios = models.TextField(max_length=200)
    entrada = models.DateField(auto_now_add=True,blank=True)
    prazo_entrega = models.DateField(blank=True,null=True)
    data_finalizacao = models.DateField(blank=True,null=True)

    def get_editar_ordem(self):
        return reverse('editar_ordem',kwargs={'id':self.id})
    def get_del_ordem(self):
        return reverse('deletar_ordem',kwargs={'id':self.id})

    def __str__(self):
        return "OS do cliente: "+str(self.cliente.nome)+" | "+self.status

    @property
    def status(self):
        return "finalizado" if self.data_finalizacao else "não finalizado"

class Orcamento(models.Model):
    ordem_servico = models.ForeignKey(OrdemDeServico,on_delete=models.PROTECT,blank=True,null=True)
    quantidade = models.IntegerField()
    pecas = models.TextField(max_length=200)
    servicos = models.TextField(max_length=500)
    valor_mao_de_obra = models.FloatField(blank=True,null=True)
    previsao_entrega = models.DateField(blank=True,null=True)
    data_saida = models.DateField(blank=True,null=True)
    total_a_pagar = models.DecimalField(decimal_places=2,max_digits=8)

    def __str__(self):
        return "valor orçamento | "+str(self.valor_mao_de_obra)

    def get_editar_orcamento(self):
        return reverse('editar_orcamento',kwargs={'id':self.id})
    
