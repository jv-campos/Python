print('=='*11)
print('OS 10 TERMOS DE UMA PA')
print('=='*11)

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite uma razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo, razao):
    print('{} '.format(c), end=('-> '))
print('ACABOU')
