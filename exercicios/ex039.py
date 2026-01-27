from datetime import date

data = int(input('Qual o ano em que você nasceu: '))
atual = date.today().year
alistamento = atual - data

if alistamento == 18:
    print('Você tem {} anos, esta na hora de se alistar'.format(alistamento))
elif alistamento < 18:
    saldo = 18 - alistamento 
    ano = atual + saldo 
    print('Você tem {} anos, ainda vai se alistar daqui a {} anos'.format(alistamento, saldo ))
    print('Seu ano de alistamento vai ser {}'.format(ano))
else:
    saldo = alistamento - 18
    ano = atual - saldo 
    print('Você tem {} anos, deveria ter se alistado há {} anos atras'. format(alistamento, saldo))
    print('Seu ano de alistamento vai ser {}'.format(ano))
