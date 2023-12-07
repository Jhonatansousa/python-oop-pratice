from classes import *


#primeiro criei um cliente
cliente1 = Cliente(1, 'primeiro', 'rua 1')
#com o cliente criado, posso criar uma conta
conta1 = Conta(cliente1, 1, 100)

cliente2 = Cliente(2, 'segundo', 'rua 2')
conta2 = Conta(cliente2, 2, 50)

def sacarValor(conta, valor):
  
  conta.sacar(valor)
  print(conta.saldo)
  
def depositarValor(conta, valor):
  conta._depositar(valor)
  print(conta.saldo)


def transferirValor(contaRementente, contaDestinataria, valor):
  if contaRementente.saldo >= valor:
    contaRementente.transferir(contaDestinataria, valor)
    #linha abaixo apenas para controle e verificação do saldo das contas
    print(contaRementente.saldo, contaDestinataria.saldo)
  else:
    print('Saldo insuficiente para realizar a transferêcia')

def consultarExtrato(conta):
  return conta._historico.extrato()

if __name__ == '__main__':
  sacarValor(conta1, 19)
  depositarValor(conta1, 2333)
  transferirValor(conta1, conta2, 52)  
  consultarExtrato(conta1)
  print(Conta._quantidadeContas)