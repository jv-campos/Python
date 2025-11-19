preco = float(input('Qual o preço do seu produto? '))
desconto = preco - (preco * 5 / 100)
print( 'O produto que custava {} agora esta por {}'
      .format(preco, desconto))