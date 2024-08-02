resp = 'S'
soma = quant = media = maior = menor = 0

while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar [S/N]: ')).strip().upper()

media = soma / quant
print(f'Media é {media}')
print(f'O maior numero é: {maior}, e o menor numero é {menor}')
print('fim do programa')