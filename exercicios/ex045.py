from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Qual sua escolha
[ 0 ] Pedra 
[ 1 ] Papel
[ 2 ] Tesoura
''')
jogada = int(input('Digite a sua escolha: '))
print('-=' * 12)
print('O computador jogou {} \nVocê jogou {}'.format(itens[computador], itens[jogada]))
print('-=' * 12)
if jogada == 0: #pedra
    if computador == 0:
        print('Empate')
    elif computador == 1:
        print('Computador venceu')
    elif computador == 2:
        print('Você venceu')
elif jogada == 1:#papel
    if computador == 0:
        print('Você venceu')
    elif computador == 1:
        print('Empate')
    elif computador== 2:
        print('computador venceu') 
elif jogada == 2: #tesoura 
    if computador == 0:
        print('computador venceu')
    elif computador == 1:
        print('Você venceu')
    elif computador== 2:
        print('Empate')
else:
    print('Jogada invalida')
