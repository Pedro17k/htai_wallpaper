ano = int(input('Digite um ano: '))

if ano / 4:
    print('\033[4;32mAno é bissexto')
else:
    print('Este ano não é bissexto')