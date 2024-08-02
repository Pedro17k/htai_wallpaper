data = int(input('Qual a data de nascimento: '))
categoria = 2024 - data
if categoria <= 9:
    print('Classificação "MIRIM"')
elif categoria <= 14:
    print('Classificação "INFANTIL"')
elif categoria <= 19:
    print('Classificação "JUNIOR"')
elif categoria <= 25:
    print('Classificação "SENIOR"')
else:
    print('Classificação "MASTER"')
