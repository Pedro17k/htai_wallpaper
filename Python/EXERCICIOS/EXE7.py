salario = float(input('Digite o valor do salario: '))
if salario > 1250.00:
   aumento = salario * (10 / 100)
   print('O aumento é de: {}'.format(aumento))
else:
  aumento = salario * (15 / 100)
  print('O aumento é de: {}'.format(aumento))