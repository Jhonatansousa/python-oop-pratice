#criando uma classe
from datetime import date
class Pessoa:
  def __init__(self, nome, ano_nas, endereco):
    self.nome = nome
    self.ano_nas = ano_nas
    self.endereco = endereco
  
  def apresentar(self):
    self.endereco.apresentar_endereco()
  #método estático
  @staticmethod
  def idade(ano_nas):
    return date.today().year - ano_nas

#criando uma Herança

class Aluno(Pessoa):
  def __init__(self, nome, ano_nas, matricula):
    super().__init__(nome, ano_nas)
    self.matricula = matricula

  def apresentar_aluno(self):
    super().apresentar()
    print(f'e a matrícula é: {self.matricula}')

#criando uma Agregação

class Endereco:
  def __init__(self, rua, cidade, cep):
    self.rua = rua
    self.cidade = cidade
    self.cep = cep

  def apresentar_endereco(self):

    print(f'endereco é rua: {self.rua} da cidade de: {self.cidade} e cep: {self.cep}')


