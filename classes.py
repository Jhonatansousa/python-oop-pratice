
class Endereco:
  def __init__(self, cep, rua, cidade):
    self.cep = cep
    self.rua = rua
    self.cidade = cidade
    
#a classe endereço está agregada à classe Cliente(endereco entra nos parametros da instância de cliente)
class Cliente:
  def __init__(self, cpf, nome, endereco):
    self.cpf = cpf
    self.nome = nome
    self.endereco = endereco
#a classe Cliente está agregada à classe Conta (ela entra nos parâmetros da instância)
class Conta:
  def __init__(self,clientes, numero, saldo = 0.0):
    self.clientes = clientes
    self.numero = numero
    self.saldo = saldo
    #a linha abaixo é onde fiz uma composição (Extrato())
    self.transacoes = Extrato()
  def depositar(self, valor):
    if valor > 0:
      self.saldo += valor
      return f'Depósito concluído, saldo total da conta: R${self.saldo}'
      
  def sacar(self, valor):
    if valor < self.saldo:
      self.saldo -= valor
      return f'Saque no valor de R${valor} concluído, saldo atual de: R${self.saldo}'
    
    else:
      return 'Saldo insuficiente'

  def transferir(self, contaDestino, valor):
    if valor < self.saldo and valor > 0:
      contaDestino.depositar(valor)
      self.saldo -= valor
      return 'transferência concluída!'
    else:
      return 'Saldo insuficiente!'


class Extrato:
  def __init__(self):
    self.transacoes = []

  def extrato(self):
    for movimentacao in self.transacoes:
      print(f'')
