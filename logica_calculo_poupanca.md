## LÓGICA DO CÁLCULO DO RENDIMENTO DA POUPANÇA
***regras***
o rendimento é creditado na conta no aniversário da aplicação
exemplo: se depositou dia 19, todo dia 19 será creditado rendimento
se o aniversário da poupança coincidir com um final de semana ou feriado, o rendimento será creditado no próximo dia útil

***cálculo do rendimento***
eu pego o saldo da poupança
eu passo ela como um saldo anterior
se houver saque dentro de 30 dias, eu pego esse novo valor e calculo o rendimento com esse saldo novo
se houver deposito, eu ignoro o valor adicionado e calculo o rendimento
***fórmula do calculo***
rendimentoMensal = (saldoAnterior * (0,5%/12)) + (saldoAnterior * TaxaReferencialMensal)
é usado 0,5% pois a taxa selic é maior que 8,5% ao ano


**taxa atual 2023**
taxa selic atual é de 13,5%
taxa referencial atual é de 0,5029%
no caso, como a taxa selic é maior que 8,5% ao ano, entao a taxa da poupança será 0,5% + 0,5%(arredondando)

**Regras da Taxa Fixa e Variável**
***Taxa Fixa*** (quando a Selic é menor ou igual a 8,5% ao ano): 70% da taxa Selic ao ano mais a Taxa Referencial (TR).
***Taxa Variável*** (quando a Selic é maior que 8,5% ao ano): 0,5% ao mês mais a TR.


