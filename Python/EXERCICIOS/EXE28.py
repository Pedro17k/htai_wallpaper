TOTAL = maisdemil = menor = cont =  0
barato = ' '

while True:
    produto = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o preço do produto: '))
    cont += 1
    TOTAL += preço
    if preço > 1000:
        maisdemil += 1
    
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total da compra é: {TOTAL}')
print(f'Produto que custam mais de mil: {maisdemil}')
print(f'Temos: {menor} foi o: {barato}')
print('FIM DO PROGRAMA!')