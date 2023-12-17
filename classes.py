import time
dataAtual = time.strftime("%d/%m/%Y - %H:%M:%S")

class Endereco:
  def __init__(self, cep, rua, cidade):
    self._cep = cep
    self._rua = rua
    self._cidade = cidade
    
#a classe endereço está agregada à classe Cliente(endereco entra nos parametros da instância de cliente)
class Cliente:
  def __init__(self, cpf, nome, endereco):
    self._cpf = cpf
    self._nome = nome
    self._endereco = endereco
#a classe Cliente está agregada à classe Conta (ela entra nos parâmetros da instância)
class Conta:
  _quantidadeContas = 0
  def __init__(self,clientes, numeroConta, saldo = 0.00):
    self._clientes = clientes
    self._numeroConta = numeroConta
    self.__saldo = saldo
    #a linha abaixo é onde fiz uma composição instanciando Historico dentro de Conta (Historico())
    self._historico = Historico ()
    Conta._quantidadeContas += 1

  @property
  def saldo(self):
    return self.__saldo
  
  
  def _depositar(self, valor):
    if valor > 0:
      self.__saldo += valor
      self._historico.transacoes.append(['DEPÓSITO', valor, 'DATA', dataAtual])
      return f'Depósito concluído, saldo total da conta: R${self.__saldo}'

      
  def _sacar(self, valor):
    if valor < self.__saldo:
      self.__saldo -= valor
      self._historico.transacoes.append(['SAQUE', valor, 'DATA', dataAtual])
      return f'Saque no valor de R${valor} concluído, saldo atual de: R${self.__saldo}'
    
    else:
      return 'Saldo insuficiente'
  
  
  def _transferir(self, contaDestino, valor):
    if valor < self.__saldo and valor > 0:
      contaDestino._depositar(valor)
      self.__saldo -= valor
      self._historico.transacoes.append(['TRANSFERÊNCIA', valor, 'DATA', dataAtual])
      return 'transferência concluída!'
    else:
      return 'Saldo insuficiente!'


class Historico:
  def __init__(self):
    self.transacoes = []

  def _extrato(self):
    for itemTransacao in self.transacoes:
      #"{:,.2f}".format = formatação de string usando vírgula como separador de milhar e o 2f == 2 casas decimais(float)
      print(f'{itemTransacao[0]}: R${"{:,.2f}".format(itemTransacao[1])} | {itemTransacao[2]}: {itemTransacao[3]}')
      

class RendimentoPoupanca:
  def __init__(self, taxaSelic, taxaReferencialMensal):
    self.taxaSelic = taxaSelic / 100
    self.taxaReferencialMensal = taxaReferencialMensal / 100

  def calcularTaxaRemuneracao(self):
    if self.taxaSelic <= (8.5 / 100):
      taxaRemuneracao = (self.taxaSelic * 0.7) + self.taxaReferencialMensal
      return taxaRemuneracao
    taxaRemuneracao = 0.005 + self.taxaReferencialMensal
    return taxaRemuneracao

class Poupanca:
  def __init__(self, taxaRemuneracaoMes, statusConta = False, saldoPoupanca = 0.00):
    self.taxaRemuneracaoMes = taxaRemuneracaoMes
    self.saldoPoupanca  = saldoPoupanca
    self.statusConta = statusConta
    self.rendimentoPoupanca = RendimentoPoupanca ()

def abrirContaPoupanca(self):
  self.statusConta = True
  return self.statusConta

class ContaRemuneradaPoupanca(Conta, Poupanca):
  def __init__(self, clientes, numeroConta, saldo, taxaRemuneracaoMes, saldoPoupanca, statusConta, dataAbertura):
    Conta.__init__(self, clientes, numeroConta, saldo)
    Poupanca.__init__(self, taxaRemuneracaoMes, saldoPoupanca, statusConta)
    self.dataAbertura = dataAbertura

  def remunerarConta(self):
    self.saldoPoupanca += self.saldoPoupanca * (self.taxaRemuneracaoMes / 30)
    self.saldoPoupanca -= self.taxaRemuneracaoMes

  def resgatar(self):
    pass

  def aplicar(self):
    pass
