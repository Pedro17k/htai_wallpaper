import random

numero_secreto = random.randint(0,10)

tentativa = 0

print('Tente adivinhar o numero secreto de 0 a 10')

palpite = int(input('Qual seu palpite? '))
tentativa += 1

while palpite != numero_secreto:
    palpite = int(input('Errou! Tente novamente:'))
    tentativa += 1
    if palpite == numero_secreto:
        print('Parabens! Você acertou o número secreto! Seu numero de tentativas foi {}'.format(tentativa))
        break

if tentativa == 1:
    print('Parabens você acertou o número secreto na primeira tentativa!')


