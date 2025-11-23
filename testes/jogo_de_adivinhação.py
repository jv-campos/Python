from random import choice


vidas = 5 # "Vidas" do jogador
while vidas >= 1:
    list = [1, 2, 3, 4, 5]
    sorteio = choice(list) # Escolhe um número aleatorio da lista
    numero = int(input('Em qual número estou pensando: '))
    if numero == sorteio:
        print('Parabens você acertou!!!!!!!!')
        break
    else:
        print('Que pena você errou!! O número era {} e não {}'.format(sorteio, numero))
        vidas -= 1
        print(f'Você so tem mais {vidas} chances')
print('Fim do programa')