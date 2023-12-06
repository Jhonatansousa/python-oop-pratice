import time
dataAtual = time.strftime("%d/%m/%Y - %H:%M:%S")

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
  def __init__(self,clientes, numeroConta, saldo = 0.0):
    self.clientes = clientes
    self.numeroConta = numeroConta
    self.saldo = saldo
    #a linha abaixo é onde fiz uma composição (Historico())
    self.historico = Historico ()
  def depositar(self, valor):
    if valor > 0:
      self.saldo += valor
      self.historico.transacoes.append(['DEPÓSITO', valor, 'DATA', dataAtual])
      return f'Depósito concluído, saldo total da conta: R${self.saldo}'
      
  def sacar(self, valor):
    if valor < self.saldo:
      self.saldo -= valor
      self.historico.transacoes.append(['SAQUE', valor, 'DATA', dataAtual])
      return f'Saque no valor de R${valor} concluído, saldo atual de: R${self.saldo}'
    
    else:
      return 'Saldo insuficiente'

  def transferir(self, contaDestino, valor):
    if valor < self.saldo and valor > 0:
      contaDestino.depositar(valor)
      self.saldo -= valor
      self.historico.transacoes.append(['TRANSFERÊNCIA', valor, 'DATA', dataAtual])
      return 'transferência concluída!'
    else:
      return 'Saldo insuficiente!'


class Historico:
  def __init__(self):
    self.transacoes = []

  def extrato(self):
    for itemTransacao in self.transacoes:
      #"{:,.2f}".format = formatação de string usando vírgula como separador de milhar e o 2f == 2 casas decimais(float)
      print(f'{itemTransacao[0]}: R${"{:,.2f}".format(itemTransacao[1])} | {itemTransacao[2]}: {itemTransacao[3]}')
      
