n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
from time import sleep
opção = 0
while opção != 5:
    print('''          [ 1 ] multiplicar
          [ 2 ] maior 
          [ 3 ] somar
          [ 4 ] novos numeros
          [ 5 ] sair do programa ''')
    
    opção = int(input('Qual é sua opção? '))
    if opção == 1:
        multiplicar = n1 * n1
        print('O resultado da multiplicação de {} e {} é igual a {}'.format(n1, n2, multiplicar))
    elif opção == 2:
        if n1 > n2:
            print(f'O maior é {n1}')
        else:
            print(f'O maior é {n2}')
    elif opção == 3:
        somar = n1 + n2
        print(f'A soma de {n1} + {n2} é igual a {somar}')
    elif opção == 4:
        print('Informe os numeros novamente: ')
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segundo numero: '))
    elif opção == 5:
        print('FINALIZANDO...')
    else:
        print('OPÇÃO INVALIDA. TENTE NOVAMENTE')
    print('=-=' * 10)
    sleep(2)
print('PROGRAMA FINALIZADO.')

