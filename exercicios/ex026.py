frase = str(input('Digite uma frase: ')).strip()
print('A letra A aparece {} vezes'.format(frase.lower().count('a')))
print('A primeira letra A aparece pela primeira vez na posição {}'
      .format(frase.lower().find('a') + 1))
print('A letra A apareceu pela ultima vez na posição {}'
      .format(frase.lower().rfind('a') + 1))
