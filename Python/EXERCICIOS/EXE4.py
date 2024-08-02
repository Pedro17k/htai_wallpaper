viagem = float(input('Qual a distacia do seu destino? '))
if viagem < 200:
    distancia = viagem * 0.50
    print('Seu destino ficara: {}'.format(distancia))
else: 
    distancia2 = viagem * 0.45
    print('Seu destino ficara: {}'.format(distancia2))