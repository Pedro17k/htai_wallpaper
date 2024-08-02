termo = int(input('Digite o primeiro termo de progressão: '))
razão = int(input('Digite a razão da progressão: '))
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} ->', end=' ')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos mais você quer ver? '))
print(f'Você mostrou {total} progressões')
print('FIM')
