numero = int(input('Me diga um número: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('O número {}'.format(numero))
print(f'Tem {u} unidades \nTem {d} dezenas \nTem {c} centenas \nTem {m} milhares')
