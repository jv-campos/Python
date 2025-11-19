from random import shuffle
al1 = input('Qual o nome do primeiro aluno: ')
al2 = input('Qual o nome do segundo aluno: ')
al3 = input('Qual o nome do terceiro aluno: ')
al4 = input('Qual o nome do quarto aluno: ')

lista = [al1, al2, al3, al4]
shuffle(lista)

print('A ordem de apresentação do trabalho sera')
print(lista)