n1 = int(input('Digite um numero: '))
c = n1
f = 1
print(f'Fatorial de {n1}! = ', end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')