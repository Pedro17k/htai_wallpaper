for c in range(6):
    num = int(input('Digite o numero: '))
    if num % 2 == 0:
        print('A soma é {} + {} ='.format(num, num), num + num)
    else:
        print(num, 'não é par')