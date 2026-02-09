soma = 0
cont = 0 
for contagem in range(1, 501, 2):
    if contagem % 3 == 0:
        cont = cont + 1
        soma = soma + contagem
print('A soma de todos os {} valores solicitados é {}'.format( cont, soma))