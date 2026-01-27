escolha = int(input('Digite um número: '))
print(('''Escolha a base de conversão:
[ 1 ] BINÁRIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL'''))
opçao = int(input('Sua opção: '))

if opçao == 1:
    print('O {} convertido para binário é {}'.format(escolha, bin(escolha) [2: ]))
elif opçao == 2:
    print('O {} convertido para octal é {}'.format(escolha, oct(escolha)[2: ]))
elif opçao == 3:
    print('O {} convertido para hexadecimal é {}'.format(escolha, hex(escolha) [2: ]))
else:
    print('Não consegui identificar o sua escolha.')
