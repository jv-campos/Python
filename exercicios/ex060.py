n = int(input('Digite um número para calcular o seu fatorial: '))
f = 1
c = n
print(f'Calculando o fatorial de {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')