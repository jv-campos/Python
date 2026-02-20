import datetime
atual = datetime.day().year
maior = 0
for data in range(1,8):
    num = int(input('Em que ano a {}° nasceu: '.format(data)))
    
    if num - atual == 18:
        maior += 1
print('O número de pessoas maior de idade é: {}'.fomrat(maior))