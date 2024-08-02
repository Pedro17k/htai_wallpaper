somaidade = 0
media = 0
maioridadeH = 0
nomedohomen = ''
totalmu = 0

for p in range(1, 5):
    print('----- {} PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]')).strip().upper()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadeH = idade
        nomedohomen = nome
    if sexo in 'Mm' and idade > maioridadeH:
        maioridadeH = idade
        nomedohomen = nome
        media = somaidade / 4
    if sexo in 'Ff' and idade < 20:
        totalmu += 1

print('A media de idade é de {} anos'.format(media))

print('O homem mais velho é {} e tem {} anos'.format(nomedohomen,maioridadeH))

print('Temos {} mulheres com menos de 20'.format(totalmu))