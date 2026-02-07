from random import choice
from time import sleep
pontos = 0 
print('Olá, eu me chamo Hugo')
print('Vamos jogar pedra, papel e tesolra ? ')
jogo = int(input('Se quider digite 1 se não quiser digite 2: '))

if jogo == 1:
    while pontos < 1:
        jogo = [1, 2, 3]
        print("""
            [ 1 ] Predra 
            [ 2 ] Papel
            [ 3 ] Tesolra
            """)
        jogador = int(input('Qual você vai jogar? '))
        Hugo = choice(jogo)
        print('Calma que estou escolhendo...')
        sleep(2)
        print('')
        if Hugo == jogador:
            print('Hugo escolheu {}, e você esoclheu {}. Empate'.format(Hugo, jogador))
        elif Hugo == 1 and jogador == 2:
            print('Hugo escolheu {}, e você esoclheu {}. Você ganhou!!!'.format(Hugo, jogador))
            pontos += 1
            break
        elif Hugo == 1 and jogador == 3:
            print('Hugo escolheu {}, e você esoclheu {}. Hugo ganhou!!!'.format(Hugo, jogador))
            pontos += 1 
            break
        elif Hugo == 2 and jogador == 1:
            print('Hugo escolheu {}, e você esoclheu {}. Hugo ganhou!!!'.format(Hugo, jogador))
            pontos += 1
            break
        elif Hugo == 2 and jogador == 3:
            print('Hugo escolheu {}, e você esoclheu {}. Você ganhou!!!'.format(Hugo, jogador))
            pontos += 1 
            break
        elif jogador == 1 and Hugo == 2:
            print('Hugo escolheu {}, e você esoclheu {}. Você ganhou!!!'.format(Hugo, jogador))
            pontos += 1
            break
        elif jogador == 1 and Hugo == 3:
            print('Hugo escolheu {}, e você esoclheu {}. Hugo ganhou!!!'.format(Hugo, jogador))
            pontos += 1 
            break
        elif jogador == 2 and Hugo == 1:
            print('Hugo escolheu {}, e você esoclheu {}. Hugo ganhou!!!'.format(Hugo, jogador))
            pontos += 1
            break
        elif jogador == 2 and Hugo == 3:
            print('Hugo escolheu {}, e você esoclheu {}. Você ganhou!!!'.format(Hugo, jogador))
            pontos += 1 
            break
elif jogo == 2:
    print('Ok, Vamos jogar outro dia')