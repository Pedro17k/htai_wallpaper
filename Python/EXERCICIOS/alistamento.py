ano = int(input('Digite seu ano de nascimento: '))

idade = 2024 - ano

if idade < 18:
    falta = 18 - idade
    print('Você ainda não precisa se alistar falta {}'.format(falta))

elif idade == 18:
    print('Está na hora de se alistar ')

else:
    atraso = idade - 18
    print('Você está atrasado {} anos'.format(atraso))