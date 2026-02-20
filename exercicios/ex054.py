from datetime import date
atual = date.today().year
maior = 0
menor = 0 
for data in range(1,8):
    num = int(input('Em que ano a {}° nasceu: '.format(data)))
    idade = num - atual
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('{} Pessoas são maior de idade'.format(maior))
print('{} pessoas são menor de idade'.format(menor))