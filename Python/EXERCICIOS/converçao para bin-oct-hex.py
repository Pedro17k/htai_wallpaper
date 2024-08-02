num = int(input('Digite um numero: '))
print('''Escolha a conversão desejada: 
[ 1 ] binario
[ 2 ] octal 
[ 3 ] hexadecimal''')

opcao = input('Qual sua opção: ')

if opcao == '1':
    print('RESULTADO: {}'.format(bin(num)[2:]))
elif opcao == '2':
    print('RESULTADO: {}'.format(oct(num)[2:]))
elif opcao == '3':
    print('RESULTADO: {}'.format(hex(num)[2:]))

else:
    print('Numero inválido. Escolha entre (1, 2 ou 3)')

