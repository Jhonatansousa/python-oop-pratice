#criando uma classe
class Pessoa:
  def __init__(self, nome, idade, endereco):
    self.nome = nome
    self.idade = idade
    self.endereco = endereco
  
  def apresentar(self):
    print(f'{self.nome} tem {self.idade} ano(s)!')
    self.endereco.apresentar_endereco()

#criando uma Herança

class Aluno(Pessoa):
  def __init__(self, nome, idade, matricula):
    super().__init__(nome, idade)
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


end = Endereco('rua 1', 'angra dos reis', 2390000)
pessoa1 = Pessoa('jhonatan', 27, end)
pessoa1.apresentar()