sexo = str(input('Qual seu sexo [M/F]: ')).strip().upper()[0]
s = 1
'F' = 'M' = 0
while s not in 'MmFf':
    s = str(input('Dados inválidos. Informe o seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado.'.format(s))
   


