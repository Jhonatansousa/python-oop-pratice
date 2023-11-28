from classes import Pessoa
from classes import Aluno
from classes import Endereco

end = Endereco('rua 1', 'angra dos reis', 2390000)
pessoa1 = Pessoa('jhonatan', 1996, end)
pessoa1.apresentar()
pessoa3 = Pessoa.idade(1996)
print(pessoa3)