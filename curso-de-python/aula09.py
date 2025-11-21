frase = 'alo alo papai'

# a contaagem sempre começa no 0
print(frase[4:13])

# esse codigo a baixo pega o caracter 4 ate o 13 pulando de 2 em 2 
print(frase[4:13:2])

# quando você não diz onde começar ele começa do inicio ate onde você mandar
print(frase[:9])

# quando você não diz onde termina ele pega de onde você mandar e vai ate o final
print(frase[8:])

# esse codigo a baixo pega o caracter do inicio ate o final pulando de 3 em 3 
print(frase[0::3])

# Análise
# len mostra o comprimento da frase
print(len(frase))

# count serve para contar algo
print(frase.count('a'))

# análise com fatiamento
print(frase.count('a', 8, 13))

# find me retorna o valor onde se encontra a palavra desejada 
print(frase.find('papai'))

# se o valor passado não existir ele retorna -1
print(frase.find('abacate'))