valor = float(input('Qual o valor da casa ?'))
salario = float(input('Qual seu salário? '))
anos = int(input('Em quantos anos você vai conseguir pagar? '))

valor_emprestimo = valor / anos

if valor_emprestimo <= salario * 0.3:
    print('Aprovado! ')
else:
    print('Negado!')