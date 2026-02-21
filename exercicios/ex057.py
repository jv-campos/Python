sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo [M/F]: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')


# while True:
#     sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
#     if sexo in 'Mm':
#         print('Sexo Masculino confirmado com sucesso')
#         break
#     elif sexo in 'Ff':
#         print('Sexo Feminino confirmado com sucesso')
#         break
#     else:
#         print('Sexo não identificado, tente novamente')
