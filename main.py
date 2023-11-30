import time
from classes import *
tempoAtual = time.strftime("%d/%m/%Y - %H:%M:%S")

print(tempoAtual)

#primeiro criei um cliente
cliente1 = Cliente(1, 'primeiro', 'rua 1')
#com o cliente criado, posso criar uma conta
conta1 = Conta(cliente1, 1, 100)

cliente2 = Cliente(2, 'segundo', 'rua 2')
conta2 = Conta(cliente2, 2, 50)

print(conta1.saldo, conta2.saldo)

def sacar(conta, valor):
  conta.sacar(valor)
  print(conta.saldo)
  
sacar(conta2, 45)



def depositar(conta, valor):
  conta.depositar(valor)
  print(conta.saldo)

depositar(conta1, 239)



def transferir(contaRementente, contaDestinataria, valor):
  if contaRementente.saldo >= valor:
    contaRementente.transferir(contaDestinataria, valor)
    #linha abaixo apenas para controle e verificação do saldo das contas
    print(contaRementente.saldo, contaDestinataria.saldo)
  else:
    print('Saldo insuficiente para realizar a transferêcia')

transferir(conta1, conta2, 224)

