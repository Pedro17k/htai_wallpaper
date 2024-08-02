velocidade = float(input('Velocidade: '))
if velocidade > 80:
    multa = 7.00 * (velocidade - 80)
    print('Você foi multado! O valor da multa é R${}'.format(multa))
else:
    print('sem multa')