velocidade = float(input('Qual a velocidade do carro? '))
if velocidade <= 80:
    print('Tenha um bom dia, dirija com segurança.')
else:
    multa = (velocidade - 80 ) * 7
    print('Multado, o limite permitido é de 80km/h. Devera pagar R${:.2f}'.format(multa))