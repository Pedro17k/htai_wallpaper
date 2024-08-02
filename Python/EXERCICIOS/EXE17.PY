from datetime import date
atual = date.today().year

maior_idade = 0
menor_idade = 0

for d in range(1, 8):
        data = int(input('Digite o ano que a {} pessoa nasceu? '.format(d)))

        idade = atual - data

        if idade >= 21:
                maior_idade += 1
        else:
                menor_idade += 1

print('{} pessoas são maiores de idade.'.format(maior_idade))
print('{} pessoas são menores de idade.'.format(menor_idade))
                