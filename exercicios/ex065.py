res ='S'
soma = 0
quant = 0
media = 0
maior = 0
menor = 0

while res in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num 
    else :
        if num > maior:
            maior + num 
        if num < menor:
            menor = num 

    res = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
print('ACABOU')
media = soma / quant
print(f'Você digitou {quant} número e a média foi {media}')
print(f'O maior valor foi {maior} o menor foi {menor}')