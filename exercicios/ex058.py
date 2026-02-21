from random import randint
from time import sleep

# O número de chamces que você tentou (palpite)
palpite = 0

# Escolhendo um número aleatorio da lista
sorteio = randint(0,10)
print('Sou seu computador e estou pensando em um número entre 0 e 10.')
print('Será que você consegue acertar ? ')
sleep(2)

# loop do jogo 
while True:
    numero = int(input('Em qual número estou pensando: '))
    if numero == sorteio:
        print('Parabens você acertou!!!!!!!!')
        palpite += 1 
        break
    elif numero < sorteio:
        print('Mais que isso')
        palpite += 1
    elif numero > sorteio:
        print('Menos que isso')
        palpite += 1 
print('Fim do programa. Você acertou em {} palpites'.format(palpite))