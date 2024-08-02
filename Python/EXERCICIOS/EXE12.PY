num = int(input('Digite um numero para ver a tabuada: '))

print('TABUADA:\n')
for c in range(0, 11):
    print(f'{num} * {c} == {num * c}')