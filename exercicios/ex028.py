from random import choice
print('-=--=' * 28)
print('Estou pensando em um número de 0 a 5')
print('-=--=' * 28)
list = [1, 2, 3, 4, 5]
sorteio = choice(list) # Escolhe um número aleatorio da lista
numero = int(input('Em qual número estou pensando: '))
if numero == sorteio:
    print('Parabens você acertou!!!!!!!!')
else:
    print('Que pena você errou!! O número era {} e não {}'.format(sorteio, numero))
