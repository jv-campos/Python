num = int(input('Digite um número: '))

for tabuada in range(0, 11):
    soma = num * tabuada
    print('{} x {:2} = {}'.format(num, tabuada, soma))