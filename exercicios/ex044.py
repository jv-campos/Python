preço = float(input('Informe o preço do seu produto: '))
print("""
      [ 1 ] Pagamento à vista dinheiro/cheque
      [ 2 ] Pagamento à vista no cartão
      [ 3 ] Pagamento parcelado 2x cartão
      [ 4 ] Pagamento parcelado 3x ou mais cartão
      [ 0 ] Cancelar compra
      """)
opçao = int(input('Informe a forma de pagamento: '))

if opçao == 1:
    desconto = preço - (preço * 0.1)
    print('Você teve 10% de desconto, seu produto esta custando R${:.2f}'.format(desconto))
elif opçao == 2:
    desconto = preço - (preço * 0.05)
    print('Você teve 5% de desconto, seu produtp esta custando R${:.2f}'.format(desconto))
elif opçao == 3:
    print('Seu produto esta custando R${:.2f}'.format(preço))
elif opçao == 4:
    juros = preço + (preço * 0.2)
    print('Cobramos 20% de desconto, seu produto esta custando R${:.2f}'.format(juros)) 
elif opçao == 0:
    print('Ok, vamos cancelar sua compra')