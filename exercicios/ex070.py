total = preçomil = menor = cont =  0
barato = ' '
while True:
    produto = str(input('Digite o nome do produto : '))
    preço = float(input('Digite o preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        preçomil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto

    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar ? [S/N]: ')).strip().upper()[0]
    if res == 'N':
        break
print('FIM DO PROGRAMA')
print(f'O tatal gasto foi de R${total:.2f}')
print(f'{preçomil} produtos acima de R$1000')
print(f'O produto mair barato foi {barato} custando R${menor:.2f}')