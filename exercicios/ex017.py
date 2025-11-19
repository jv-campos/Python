import math

cateto_adjacente = float(input('Diga o comprimento do cateto adjacente: '))
cateto_oposto = float(input('Diga o comprimento do cateto oposto: '))

equacao = math.sqrt((cateto_adjacente ** 2) + (cateto_oposto ** 2))

print('O comprimento da hipotenusa é: {:.2f}'.format(equacao))