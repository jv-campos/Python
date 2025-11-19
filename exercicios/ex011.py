largura = float(input('Qual a larguta da sua parede em metros? '))
altura = float(input('Qual a altura da sua parede? '))

print('A área da sua parede é de {}, então você precisara de {} baldes de tintas para pintar sua parede'
      .format(largura * altura, largura * altura / 2 ))
