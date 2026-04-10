

# POR ALGUM MOTIVO BUGA QUANDO ESCOLE PAR DEPOIS DE ALGUMAS JOGADAS 
# REFAZER, MAS USANDO O PROGRAMA DO GUANABARA PARA COMPARAR

# from random import choice

# ganhos = 0
# while True:
#     jogar = str(input('Quer jogar impar ou par [S/N]? ')).upper()
#     if jogar in 'Ss':
#         jogada = int(input('Escolha um número: '))
#         escolha = str(input('Quer impar ou par [I/P]:')).upper()
#         lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#         computador = choice(lista)
#         decição = (jogada + computador) % 2
#         if decição == 0 and escolha == 'P':
#             print(f'{jogada} + {computador} = {jogada + computador}')
#             print('O resultado deu Par. VOCÊ GANHOU!!!')
#             ganhos += 1
#         elif decição != 0 and escolha == 'p':
#             print(f'{jogada} + {computador} = {jogada + computador}')
#             print('O resultado deu Impar. EU GANHEI!!!')
#         if decição == 0 and escolha == 'I':
#             print(f'{jogada} + {computador} = {jogada + computador}')
#             print('O resultado deu Par. EU GANHEI!!!')
#         elif decição != 0 and escolha == 'I':
#             print(f'{jogada} + {computador} = {jogada + computador}')
#             print('O resultado deu Impar. VOCÊ GANHOU!!!')
#             ganhos += 1
#     else:
#         break
# print('Tudo bem, volte sempre')
# print(f'Você ganhou {ganhos} vezes')