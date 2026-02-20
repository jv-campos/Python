soma = 0 
media = 0 
MaiorIdadeHomem = 0
NomeVelho = ''
Mulher20 = 0
for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    soma += idade
    if p == 1 and sexo in 'Mm':
        MaiorIdadeHomem = idade
        NomeVelho = nome
    if sexo in 'Mm' and idade > MaiorIdadeHomem:
        MaiorIdadeHomem = idade
        NomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        Mulher20 += 1

media = soma / 4
print(f'A média de idade do grupo é de {media} anos')
print(f'O homem mais velho tem {MaiorIdadeHomem} e o nome dele é {NomeVelho}')
print(f'Ao todo tem {Mulher20} mulheres com menos de 20 anos')