from time import sleep
n = int(input('Digite um numero: [999 para encerrar] '))
soma = 0
c = 999
digito = 0
while c != n:
    soma = soma + n
    n = int(input('Digite um numero: [999 para encerrar] '))
    digito += 1
sleep(2)
print(f'Soma dos numeros digitados são: {soma}', f'\nForam digitados: {digito}')
print('PROGRAMA ENCERRADO!')