soma = 0
cont = 0 
for par in range(0,6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você digitou {cont} números pares e a soma ente eles é: {soma}')