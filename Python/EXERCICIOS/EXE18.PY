
maior = 0
menor = 0


for d in range(1, 6):
    peso = float(input('Digite o peso da {} pessoa: '.format(d)))

    if d == 1:
        maior = d
        menor = d
        
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}kg'.format(maior))
print('O menor peso lido foi de {}kg'.format(menor))
