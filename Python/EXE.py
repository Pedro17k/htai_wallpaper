valordacasa = float(input('Qual o valor da casa: R$ '))
salario = float(input('Qual seu salario: '))
anos = int(input('Quantos anos você pretende pagar: '))

prestação = valordacasa / (anos * 12)
minimo = salario * 30 / 100

print('Para pagar uma casa de R${} em {} anos'.format(valordacasa, anos), end='')
print(' a prestação será de R${} '.format(prestação))
if prestação <= minimo:
    print('Aprovado!')
else:
    print('REPROVADO!')