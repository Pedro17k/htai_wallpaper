frase = str(input('Digite uma frase: '))

primeiraletra = frase[0]

ultimaletra = frase[-1]

if primeiraletra == ultimaletra:
    print('É políndromo')
else:
    print('Não é polindromo')