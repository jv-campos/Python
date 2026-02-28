print('Gerador de PA')
print('-=' * 12)
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razão
        cont += 1 
    print('PAUSA')
    mais = int(input('Quantos termos a mais você quer mostrar?: '))
print(f'Você finalizou com o total de {total} termos mostrados')