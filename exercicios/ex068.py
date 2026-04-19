from random import randint
v = 0
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Você quer par ou impar? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador}, o computador {computador}. Total {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU!!!!')
            v += 1
        else:
            print('VOCÊ PERDEU!!!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU!!!!')
            v += 1
        else:
            print('VOCÊ PERDEU!!!!')
            break
print(f'Você ganhou {v} vezes')