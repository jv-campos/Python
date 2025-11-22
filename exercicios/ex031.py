viagem = float(input('Qual é a distacia da sua viagem ? '))
if viagem <= 200:
    cobrar = viagem * 0.50
    print('Sua passagem custa R${:.2f}'.format(cobrar))
else:
    cobrar = viagem * 0.45
    print('Sua passagem custa R${:.2f}'.format(cobrar))
print('Boa viagem!')