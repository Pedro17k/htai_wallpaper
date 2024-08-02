numero = int(input('Digite um numero: '))

if numero > 1:
    for divisor in range(2, numero):
        if numero % divisor == 0:
            print('{} não é um numero primo'.format(numero))
            break
    else:
        print('{} é numero primo'.format(numero))
    

else:
    print('Não é possivel determinar')