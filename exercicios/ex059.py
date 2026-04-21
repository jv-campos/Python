from time import sleep

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opção = 0

while opção != 5:
    print('''          [ 1 ] soma 
          [ 2 ] multiplicar
          [ 3 ] maior
          [ 4 ] novos números
          [ 5 ] sair do programa''')
    opção = int(input('>>>>>>>Escolha uma opção: '))
    if opção == 1:
        soma = n1 + n2
        print(f'A soma de {n1} e {n2} é {soma}')
    elif opção == 2:
        mult = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é {mult}')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior é {maior}')
    elif opção == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif opção == 5:
        print('Finalizando....')
    print('=-='*10)
sleep(2)
print('Programa finalizado com sucesso.')
