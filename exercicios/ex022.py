nome = str(input('Digite seu nome completo: ')).strip()

print('Seu nome em maiúsculo é: {}'.format(nome.upper()))
print('Seu nomr em minúsculo é: {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
# print('Seu primeiro tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))