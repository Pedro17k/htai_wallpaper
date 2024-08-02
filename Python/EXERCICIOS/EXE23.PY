from time import sleep

print('-'*30)
print('Sequencia de Fibonacci ')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))

t1 = 0 
t2 = 1
print('~'*30)
cont = 3

print(f'{t1} -> {t2}', end='')

while True:
    while cont <= n:
        t3 = t1 + t2
        print(f' -> {t3}', end='')
        cont += 1
        t1 = t2
        t2 = t3 
    print(' -> PAUSA')
    n += int(input('\nQuantos mais? '))
    if n < cont:
        break
sleep(1)
print('FIM DO PROGRAMA')
